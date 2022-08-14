from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
# Create your models here.
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
