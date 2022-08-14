from django.urls import path
from . import views



urlpatterns = [
        path('', views.audio_msg, name='audio_msg'),
        path('<int:id>', views.audio_detail, name='audio_detail')


]
