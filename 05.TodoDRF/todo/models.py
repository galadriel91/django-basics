from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    important = models.BooleanField(default=False)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title