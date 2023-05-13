import admin_thumbnails
from django.db.models import ManyToManyField
from django.forms import CheckboxSelectMultiple
from django.contrib import admin
from .models import Post, PostImage, Comment, HashTag

class CommentInline(admin.TabularInline):
    model=Comment
    extra=1

@admin_thumbnails.thumbnail('photo')
class PhotoInline(admin.TabularInline):
    model=PostImage
    extra=1    

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['id', 'user']
    inlines=[
        CommentInline,
        PhotoInline
    ]
    formfield_overrides = {
        ManyToManyField : {'widget': CheckboxSelectMultiple}
    }

@admin.register(PostImage)
class PhotoAdmin(admin.ModelAdmin):
    list_display=['id', 'photo' , 'post']

@admin.register(Comment)
class PhotoAdmin(admin.ModelAdmin):
    list_display=['id', 'user' , 'post']

@admin.register(HashTag)
class HashtagAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
