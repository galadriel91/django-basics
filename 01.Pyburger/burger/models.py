from django.db import models

# Create your models here.
class Burger(models.Model):
    title = models.CharField('햄버거 이름', max_length=20)
    price = models.IntegerField('햄버거 가격')
    calories = models.IntegerField('햄버거 칼로리')

    def __str__(self):
        return self.title