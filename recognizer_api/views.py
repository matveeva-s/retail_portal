import json
from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView

from recognizer_api.serializers import VisitSerializer, VisitsSerializer
from recognizer_api.models import Visits
from recognizer_api.pagination import VisitsPagination


def test_visit_json(request):
    fileobject = open('visit.json')
    data = json.load(fileobject)
    return JsonResponse(data)


class VisitsApi(ListAPIView):
    serializer_class = VisitsSerializer
    # queryset = Visits.objects.filter(visitequipments__supercategoryid__isnull=False)
    queryset = Visits.objects.order_by('-completiondate')
    pagination_class = VisitsPagination


class VisitApi(RetrieveAPIView):
    serializer_class = VisitSerializer
    # queryset = Visits.objects.filter(visitequipments__supercategoryid__isnull=False)
    queryset = Visits.objects.order_by('-completiondate')
