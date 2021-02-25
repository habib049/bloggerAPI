from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    birthday = models.DateField(null=True, blank=True, verbose_name="Birth day", help_text="Birth day")
    gender = models.CharField(max_length=50, choices=(('male', 'male'), ('female', 'female')), default='male',
                              verbose_name="Gender", help_text="Gender")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    profile_image = models.ImageField(upload_to='\media', null=True, blank=True)

    is_blogger=models.BooleanField(default=False,verbose_name="User is blogger", help_text="User is blogger")