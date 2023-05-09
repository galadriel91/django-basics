from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    thumbnail = models.ImageField("썸네일 이미지", upload_to='post', blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"{self.post.title}의 댓글 {self.id}입니다"    