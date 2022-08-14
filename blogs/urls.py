from django.urls import path

from . import views


urlpatterns = [
        path('', views.blogs, name='blogs'),
        path('<int:id>', views.blog_detail, name='blog_detail')


]
