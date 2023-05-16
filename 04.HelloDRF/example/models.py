from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField()
    pages = models.IntegerField()
    published_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title