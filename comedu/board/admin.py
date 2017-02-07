from django.contrib import admin
from .models import Board


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','title')

admin.site.register(Board,BoardAdmin)
# Register your models here.
