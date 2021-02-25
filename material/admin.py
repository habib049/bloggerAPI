from django.contrib import admin
from .models import Post, Category, PostTag, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'content', 'category', 'is_published']
    search_fields = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category_type', 'category_level', 'add_time', 'thumbnail']
    search_fields = ['name', 'category_type']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'add_time']
    search_fields = ['name']


@admin.register(PostTag)
class PostAdmin(admin.ModelAdmin):
    list_display = ['get_post', 'get_tag']
    search_fields = ['get_post']

    def get_post(self, obj):
        return obj.post.title

    def get_tag(self, obj):
        return obj.tag.name
