from django.contrib import admin
from .models import Post, Comment, Category, AlbumPost

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'modify_date', 'author')
    list_filter = ('modify_date',)
    search_field = ('title', 'content')

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {"slug": ("name",)}

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_filter = ('modify_date','author')

class AlbumPostAdmin(admin.ModelAdmin):
    model = AlbumPost
    list_display = ('title', 'author')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(AlbumPost, AlbumPostAdmin)
