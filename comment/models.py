from django.db import models
from material.models import Post
from users.models import UserProfile
from material.models import Post

class Comment(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.DO_NOTHING)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null= True)
    content = models.TextField(null=True)
    like_number = models.IntegerField(default=0)
    dislike_number = models.IntegerField(default=0)
    add_time = models.DateTimeField(auto_now=True, verbose_name="comment add time", help_text="comment add time")
    reply_comment = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True,
                                      related_name="reply")
    parent_comment = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True,
                                       related_name="parent")

    def __str__(self):
        return self.content
