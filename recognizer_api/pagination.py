from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class VisitsPagination(PageNumberPagination):
    page_size = 50
    page_size_query_param = 'paginate_by'
    max_page_size = 200
