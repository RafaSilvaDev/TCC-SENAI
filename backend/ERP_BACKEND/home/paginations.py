from rest_framework.pagination import PageNumberPagination


class ResponsePaginationGiant(PageNumberPagination):
    page_query = 'p'
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size: 20

class ResponsePaginationBig(PageNumberPagination):
    page_query = 'p'
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size: 12

class ResponsePaginationMedium(PageNumberPagination):
    page_query = 'p'
    page_size = 9
    page_size_query_param = 'page_size'
    max_page_size: 9

class ResponsePaginationSmall(PageNumberPagination):
    page_query = 'p'
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size: 6

class ReponsePaginationDecimal(PageNumberPagination):
    page_query = 'p'
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size: 10