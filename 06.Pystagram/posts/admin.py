import admin_thumbnails
from django.contrib import admin
from .models import Post, PostImage, Comment

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

@admin_thumbnails.thumbnail('photo')
class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id' , 'content']
    inlines = [
        CommentInline,
        PostImageInline
    ]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ['id' , 'post', 'photo']
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id' , 'post', 'content']
    pass