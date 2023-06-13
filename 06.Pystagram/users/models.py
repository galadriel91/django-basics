from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField('프로필 사진' , upload_to='users/profile' , blank=True)
    short_desc = models.TextField('짧은 소개' , blank=True)