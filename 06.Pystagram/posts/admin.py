import admin_thumbnails
from django.contrib import admin
from .models import Post, PostImage, Comment
# Register your models here.

class CommentInline(admin.TabularInline):
    extra = 1
    model = Comment

@admin_thumbnails.thumbnail('photo')
class PhotoInline(admin.TabularInline):
    extra = 1
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'content']
    inlines = [
        CommentInline, PhotoInline
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ['id' , 'post' , 'photo']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'post' , 'content']