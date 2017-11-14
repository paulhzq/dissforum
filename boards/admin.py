from django.contrib import admin
from .models import Board, Topic, Post
# Register your models here.

# @admin.register()
# class
admin.site.register(Board)
admin.site.register(Topic)
admin.site.register(Post)
