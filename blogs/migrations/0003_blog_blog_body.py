# Generated by Django 4.0.2 on 2022-08-01 18:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_remove_blog_blog_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_body',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
    ]
