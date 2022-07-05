from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView
from rest_framework import generics, permissions
from rest_framework.response import Response

from scan_and_train.models import Sku, Manafacturer
from recognizer_api.serializers import (
    VisitSerializer, VisitsSerializer, VisitProductsSerializer,
)
from recognizer_api.models import Visits
from recognizer_api.pagination import VisitsPagination, VisitsProductsPagination


class VisitsApi(ListAPIView):
    serializer_class = VisitsSerializer
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
