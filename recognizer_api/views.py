from datetime import timedelta

from django.utils import timezone
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view

from scan_and_train.models import Sku, Manafacturer
from recognizer_api.serializers import (
    VisitSerializer, VisitsSerializer, VisitProductsSerializer,
    StoreTypesOptionsSerializer, RegionsOptionsSerializer,
    StorenetworksOptionsSerializer, AddressOptionsSerializer,
    AssortmentSerializer,
)
from recognizer_api.models import Visits, Storetypes, Regions, Stores, Storenetworks
from recognizer_api.pagination import VisitsPagination, VisitsProductsPagination, ScuPagination


class VisitsApi(ListAPIView):
    serializer_class = VisitsSerializer
    # queryset = Visits.objects.filter(visitequipments__supercategoryid__isnull=False)
    queryset = Visits.objects.using('recognizer').order_by('-completiondate')
    pagination_class = VisitsPagination


class VisitApi(RetrieveAPIView):
    serializer_class = VisitSerializer
    queryset = Visits.objects.using('recognizer').order_by('-completiondate')


class VisitProductsApi(ListAPIView):
    serializer_class = VisitProductsSerializer
    pagination_class = VisitsProductsPagination

    def get_queryset(self):
        visit_id = self.kwargs.get('pk')
        barcodes = Visits.objects.using('recognizer').filter(id=visit_id).values_list(
            'visitequipments__visitbays__visitshelves__visitshelfproducts__barcode',
            'visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode'
        )
        all_barcodes = []
        [all_barcodes.extend(barcode) for barcode in barcodes]
        return Sku.objects.using('scan_and_train').filter(barcode__in=all_barcodes)


class TestClosedApi(RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        return Response({'status': 'Successful!'})


@api_view(['GET'])
def contract_matrix_options(request):
    store_types = Storetypes.objects.using('recognizer').all()
    regions = Regions.objects.using('recognizer').all()
    retailers = Storenetworks.objects.using('recognizer').all()
    addresses = Stores.objects.using('recognizer').all()
    return Response({
        'store_types': StoreTypesOptionsSerializer(store_types, many=True).data,
        'regions': RegionsOptionsSerializer(regions, many=True).data,
        'retailers': StorenetworksOptionsSerializer(retailers, many=True).data,
        'addresses': AddressOptionsSerializer(addresses, many=True).data,
    })


class RecommendedContactMatrix(ListAPIView):
    serializer_class = AssortmentSerializer
    pagination_class = ScuPagination

    def get_visits(self):
        week_ago = timezone.now() - timedelta(days=7)
        retailer_id = self.request.query_params.get('retailer')
        store_type_id = self.request.query_params.get('store_type')
        region_id = self.request.query_params.get('region')
        store_id = self.request.query_params.get('address')
        visits = Visits.objects.using('recognizer').filter(completiondate__lte=week_ago)
        # отфильтруем по параметрам наши визиты
        if retailer_id:
            visits = visits.filter(storeid__storenetworkid_id=retailer_id)
        if store_type_id:
            visits = visits.filter(storeid__storetypeid_id=store_type_id)
        if region_id:
            visits = visits.filter(storeid__cityid__regionid_id=region_id)
        if store_id:
            visits = visits.filter(storeid_id=store_id)
        return visits.distinct()

    def get_queryset(self):
        visits = self.get_visits()
        # получим все продукты в наших визитах
        barcodes = visits.filter(
            visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode__isnull=True
        ).values_list(
            'visitequipments__visitbays__visitshelves__visitshelfproducts__barcode', flat=True
        )
        correct_barcodes = visits.filter(
            visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode__isnull=False,
        ).values_list(
            'visitequipments__visitbays__visitshelves__visitshelfproducts__correctbarcode', flat=True
        )
        all_barcodes = list(set((list(barcodes) + list(correct_barcodes))))
        return Sku.objects.using('scan_and_train').filter(barcode__in=all_barcodes, name__isnull=False)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['_qs'] = self.get_visits()
        return context
