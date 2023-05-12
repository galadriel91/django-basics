import admin_thumbnails
from django.contrib import admin
from .models import Post, PostImage, Comment , HashTag
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple

class CommentInline(admin.TabularInline):
    model = Comment
    extra=1

@admin_thumbnails.thumbnail('photo')
class PhotoInline(admin.TabularInline):
    model = PostImage
    extra=1

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'content']
    inlines = [
        CommentInline, PhotoInline
    ]
    formfield_overrides = {
        ManyToManyField : {"widget":CheckboxSelectMultiple}
    }

@admin.register(PostImage)
class PhostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post' , 'photo']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'content']

@admin.register(HashTag)
class HashtagAdmin(admin.ModelAdmin):
    pass
