from django.db import models

# Create your models here.

class Burger(models.Model):
    title=models.CharField(max_length=50)
    image=models.CharField(max_length=200)
    price=models.IntegerField()
    calories=models.IntegerField()

    def __str__(self):
        return self.title