from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, Post, Topic, User


admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Topic)
