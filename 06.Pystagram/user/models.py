from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField('프로필 사진', blank=True)
    short_description = models.TextField('소개글', blank=True)