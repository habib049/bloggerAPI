from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('comments', views.CommentViewSet, basename="comments")
router.register('comment_likes',views.LikeCommentViewSet,basename="comment_like")

urlpatterns = [
    path('', include(router.urls))
]
