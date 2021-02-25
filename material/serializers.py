from rest_framework import serializers
from .models import Post, Category, Tag, PostTag


class CategorySerializerLevel2(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializerLevel1(serializers.ModelSerializer):
    sub_category = CategorySerializerLevel2(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    sub_category = CategorySerializerLevel1(many=True)

    class Meta:
        model = Category
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    num_related_posts = serializers.SerializerMethodField()

    def get_num_related_posts(self, tag):
        return len(PostTag.objects.filter(tag__id=tag.id))

    class Meta:
        model = Tag
        fields = ['name', 'add_time', 'num_related_posts']


class PostSerializer(serializers.ModelSerializer):
    tags = serializers.StringRelatedField(many=True, read_only=True)
    category = serializers.StringRelatedField(read_only=True)

    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return obj.user.username

    class Meta:
        model = Post
        fields = ['author', 'title', 'sub_title', 'content', 'category', 'tags', 'is_published', 'click_num', 'like_num',
                  'dislike_num', 'comment_num', 'add_time']
