from datetime import timedelta

from django.utils import timezone
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from scan_and_train.models import Sku
from assortment.serializers import (
    StoreTypesOptionsSerializer, RegionsOptionsSerializer,
    StorenetworksOptionsSerializer, AddressOptionsSerializer,
    ContractMatrixReadSerializer, MatrixAssortmentSerializer,
    ContractMatrixSerializer, AssortmentSerializer
)
from recognizer_api.models import Visits, Storetypes, Regions, Stores, Storenetworks
from assortment.pagination import ContractMatrixPagination
from assortment.models import RecommendedAssortment, RecommendedMatrix, ContractMatrix


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


class RecommendedMatrixCalculationView(ListAPIView):
    serializer_class = AssortmentSerializer
    pagination_class = ContractMatrixPagination

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


class RecommendedContactMatrix(ListAPIView):
    serializer_class = MatrixAssortmentSerializer
    pagination_class = ContractMatrixPagination

    def get_queryset(self):
        retailer_id = self.request.query_params.get('retailer')
        store_type_id = self.request.query_params.get('store_type')
        region_id = self.request.query_params.get('region')
        matrix = RecommendedMatrix.objects.filter(retailer=retailer_id, store_type=store_type_id, region=region_id).first()
        if matrix:
            return matrix.assortment.order_by('-distribution').all()
        return RecommendedAssortment.objects.none()


class ContractMatrixList(ListCreateAPIView):
    serializer_class = ContractMatrixReadSerializer
    pagination_class = ContractMatrixPagination
    queryset = ContractMatrix.objects.all()


class ContractMatrixCreateAPI(CreateAPIView):
    serializer_class = ContractMatrixSerializer
    pagination_class = ContractMatrixPagination
    queryset = ContractMatrix.objects.all()
