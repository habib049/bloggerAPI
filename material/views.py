from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from .serializers import CategorySerializer, TagSerializer, PostSerializer
from .models import Post, Category, Tag
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from .paginations import CustomPostPagination, CustomPageNumberPagination


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name', 'category_type']

    def get_queryset(self):
        return Category.objects.filter(category_level="1")


class TagViewSet(ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = [SearchFilter,OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['add_time']


class PostViewSet(ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPostPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'sub_title']
    ordering = '-add_time'
    ordering_fields = ['id', 'like_num', 'comment_num']
