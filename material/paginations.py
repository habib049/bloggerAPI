from rest_framework.pagination import CursorPagination, PageNumberPagination
from rest_framework.response import Response


class CustomPostPagination(CursorPagination):
    page_size = 5
    page_size_query_param = "page_size"
    ordering = ['-add_time']
    max_page_size = 50


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 5
    max_page_size = 50
