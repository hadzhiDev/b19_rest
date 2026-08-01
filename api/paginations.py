from rest_framework.pagination import PageNumberPagination


class SimplePagePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'  # клиент может менять размер: ?page_size=50
    max_page_size = 100                  # но не больше 100
    page_query_param = 'page'