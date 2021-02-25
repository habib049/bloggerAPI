
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


class CommentViewSet(ModelViewSet):

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'create':
            return CreateCommentSerializer
        return NestedCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(parent_comment=None)


class LikeCommentViewSet(CreateModelMixin, GenericViewSet):
    serializer_class = LikeCommentSerializer

    def create(self, request, *args, **kwargs):
        serialize_data = self.get_serializer(data=request.data)
        serialize_data.is_valid(raise_exception=True)
        comment_id = serialize_data.data['comment_id']
        activity = serialize_data.data['activity']
        comment = Comment.objects.get(id=comment_id)
        if bool(activity):
            comment.like_number += 1
        else:
            comment.dislike_number += 1
        comment.save()
        context = {
            'comment_id': comment_id
        }
        return Response(context, status=status.HTTP_201_CREATED)
