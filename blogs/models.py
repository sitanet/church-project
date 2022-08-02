from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


# Create your models here.
class Blog(models.Model):
    blog_catgery = (
    ('WAP', 'Word and prayer'),
    ('TSC', 'The School of Christ'),
    ('BS', 'Bible Study'),
    ('SWS', 'Sunday Worship Service'),
    ('IMGC', 'Image & Glory Conference'),
    ('KBN', 'Kingdom Business Network'),
    ('KLS', 'Kingdom Life Summit'),
    ('ETS', 'Equiping The Saint'),
    ('TEENS', 'Tenagers'),
    ('KCC', 'Kingdom Community Center'),
    )


    blog_title = models.CharField(max_length=255)
    minister_name = models.CharField(max_length=255)
    address_location = models.CharField(max_length=255)
    category = models.CharField(choices=blog_catgery, max_length=200)
    blog_photo_1 =models.ImageField(upload_to='photos/%y/%m/%d/')
    blog_photo_2 =models.ImageField(upload_to='photos/%y/%m/%d/')
    blog_photo_3 =models.ImageField(upload_to='photos/%y/%m/%d/')
    blog_photo_4 =models.ImageField(upload_to='photos/%y/%m/%d/')
    blog_photo_5 =models.ImageField(upload_to='photos/%y/%m/%d/')
    blog_body = RichTextField()
    created_date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.blog_title


class Audio_msg(models.Model):
    msg_catgery = (
    ('WAP', 'Word and prayer'),
    ('TSC', 'The School of Christ'),
    ('BS', 'Bible Study'),
    ('SWS', 'Sunday Worship Service'),
    ('IMGC', 'Image & Glory Conference'),
    ('KBN', 'Kingdom Business Network'),
    ('KLS', 'Kingdom Life Summit'),
    ('ETS', 'Equiping The Saint'),
    ('TEENS', 'Tenagers'),
    ('KCC', 'Kingdom Community Center'),
    )

    msg_title = models.CharField(max_length=255)
    minister_name = models.CharField(max_length=255)
    address_location = models.CharField(max_length=255)
    category = models.CharField(choices=msg_catgery, max_length=200)
    blog_photo_1 =models.ImageField(upload_to='photos/%y/%m/%d/')
    msg_link = models.CharField(max_length=250)
    id_link = models.CharField(max_length=200, null= True)
    created_date = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.msg_title
