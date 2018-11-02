from django.contrib import admin
# Register your models here.

from .models import Post, Job

admin.site.register(Post)
admin.site.register(Job)