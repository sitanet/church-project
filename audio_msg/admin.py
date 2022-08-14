from django.contrib import admin
from .models import Audio_msg
from django.utils.html import format_html

# Register your models here.
class Audio_msgAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.blog_photo_1.url))
    thumbnail.short_description = 'Blog Image'
    list_display = ('id','msg_title','minister_name','thumbnail','created_date')
    list_display_links = ('id', 'thumbnail', 'msg_title')
    search_fields = ('msg_title','minister_name')


admin.site.register(Audio_msg, Audio_msgAdmin)
