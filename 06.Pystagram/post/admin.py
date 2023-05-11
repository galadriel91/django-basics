from django.contrib import admin
from .models import Post, PostImage, Comment
import admin_thumbnails
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin_thumbnails.thumbnail('photo')
class PhotoInline(admin.TabularInline):
    model = PostImage
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=[
        'id', 'content'
    ]
    inlines = [CommentInline, PhotoInline]

@admin.register(PostImage)
class PhotoAdmin(admin.ModelAdmin):
    list_display=[
        'id', 'post', 'photo'
    ]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=[
        'id', 'post', 'content'
    ]        