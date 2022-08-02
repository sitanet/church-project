from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('audio_messages', views.audio_messages, name='audio_messages'),
    path('imgc', views.imgc, name='imgc'),
    path('tsc', views.tsc, name='tsc'),
    path('word_prayer', views.word_prayer, name='word_prayer'),
    path('video_messages', views.video_messages, name='video_messages'),
    path('audio_msg', views.audio_msg, name='audio_msg'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('couple_meeting', views.couple_meeting, name='couple_meeting'),
    path('kcc', views.kcc, name='kcc'),
    path('streaming', views.streaming, name='streaming'),
    path('video_streaming', views.video_streaming, name='video_streaming'),
    path('audio_streaming', views.audio_streaming, name='audio_streaming'),
]
