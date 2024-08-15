from django.contrib import admin
from .models import Blog

# Register your models here.

admin.site.register(Blog)
# class BlogAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'date_posted')