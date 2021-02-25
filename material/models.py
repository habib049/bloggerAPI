from django.db import models
from users.models import UserProfile


class Category(models.Model):
    CATEGORY_LEVEL = (
        ("1", "First level category"),
        ("2", "Second level category"),
        ("3", "Third level category")
    )
    CATEGORY_TYPE = (
        ("Technology", "Technology"),
        ("Exercise", "Exercise"),
        ("Beauty", "Beauty"),
        ("Engineering", "Engineering"),
        ("Movies", "Movies"),
        ("Travel", "Travel"),
        ("Food", "Food"),
        ("Fashion", "Fashion"),
        ("Lifestyle", "Lifestyle "),
        ("Sports", "Sports"),
        ("Music", "Music"),
    )
    name = models.CharField(max_length=100, null=False, blank=False)
    category_type = models.CharField(max_length=100, choices=CATEGORY_TYPE, null=True)
    category_level = models.CharField(max_length=100, choices=CATEGORY_LEVEL, null=True)
    parent_category = models.ForeignKey("self", null=True, blank=True, verbose_name="Parent category",
                                        help_text="Parent category",
                                        related_name="sub_category", on_delete=models.DO_NOTHING)

    add_time = models.DateTimeField(auto_now=True, verbose_name="Category add time", help_text="Category add time")
    thumbnail = models.ImageField(upload_to='media/', null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Tag name", help_text="Tag name")
    add_time = models.DateTimeField(auto_now=True, verbose_name="Tag add time", help_text="Tag add time")

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=500, verbose_name="Post title", help_text="Post title")
    sub_title = models.CharField(max_length=500, null=True, blank=True, verbose_name="Subtitle", help_text="Subtitle")
    content = models.TextField(max_length=10000)
    category = models.OneToOneField(Category, on_delete=models.DO_NOTHING, null=True, related_name='posts')
    tags = models.ManyToManyField(Tag, through="PostTag", through_fields=('post', 'tag'))
    is_published = models.BooleanField(default=False, verbose_name="Post Published")
    click_num = models.IntegerField(default=0, verbose_name="Number of clicks")
    like_num = models.IntegerField(default=0, verbose_name="Number of likes")
    dislike_num = models.IntegerField(default=0, verbose_name="Number of dislikes")
    comment_num = models.IntegerField(default=0, verbose_name="Number of comments")
    add_time = models.DateTimeField(auto_now=True, verbose_name="Post add time", help_text="Post add time")

    def __str__(self):
        return self.title


class PostTag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now=True, verbose_name="Post tag add time", help_text="post tag add time")

    def __str__(self):
        return self.tag.name
