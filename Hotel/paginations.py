from rest_framework import pagination

class HotelListPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'perpage'
    max_page_size = 50
    page_query_param = 'page'


class CityListPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'perpage'
    max_page_size = 50
    page_query_param = 'page'