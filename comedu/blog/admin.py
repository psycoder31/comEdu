from django.contrib import admin
from .models import Post, Comment

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modify_date')
    list_filter = ('modify_date',)
    search_field = ('title', 'content')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
