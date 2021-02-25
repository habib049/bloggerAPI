from rest_framework import serializers
from .models import Comment


# this is for getting comments without nested arrangement
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# this is for nested comments json
class NestedCommentSerializer(serializers.ModelSerializer):
    reply_comment = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    def get_reply_comment(self, obj):
        if obj.reply_comment is not None:
            return NestedCommentSerializer(obj.reply_comment).data
        else:
            return None

    def get_user(self,obj):
        return obj.user.username

    class Meta:
        model = Comment
        fields = '__all__'




# this is for creating a comment
class CreateCommentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        comment_object = Comment.objects.create(**validated_data)
        if comment_object.parent_comment_id:
            parent = Comment.objects.get(id=comment_object.parent_comment_id)
            parent.reply_comment = comment_object
            parent.save()
        return comment_object

    class Meta:
        model = Comment
        fields = ['content', 'reply_comment', 'parent_comment']


# this class is for like nad dislike comment
class LikeCommentSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField(required=True, label='Comment id')
    activity = serializers.BooleanField(required=True, label='like or unlike')
