from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet, basename="category")
router.register('tags', views.TagViewSet, basename="post_tags")
router.register('post', views.PostViewSet, basename="posts")

urlpatterns = [
    path('', include(router.urls))
]
