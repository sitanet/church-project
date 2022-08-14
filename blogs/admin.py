from django.contrib import admin
from .models import Blog
from django.utils.html import format_html
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.blog_photo_1.url))
    thumbnail.short_description = 'Blog Image'
    list_display = ('id','blog_title','minister_name','thumbnail','created_date')
    list_display_links = ('id', 'thumbnail', 'blog_title')
    search_fields = ('blog_title','minister_name')



admin.site.register(Blog, BlogAdmin)
