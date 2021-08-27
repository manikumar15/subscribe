from django.contrib import admin
from .models import News

# Register your models here.

class Newsadmin(admin.ModelAdmin):
    list_display = ('Email',)
admin.site.register(News, Newsadmin)