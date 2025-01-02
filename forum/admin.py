from django.contrib import admin

# Register your models here.

from .models import Category, Post, Topic

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Topic)
