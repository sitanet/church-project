from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog', views.blog, name='blog'),
    path('audio_messages', views.audio_messages, name='audio_messages'),
    path('imgc', views.imgc, name='imgc'),
    path('imgc/<int:id>', views.imgc_detail, name='imgc_detail'),
    path('tsc', views.tsc, name='tsc'),
    path('tsc/<int:id>', views.tsc_detail, name='tsc_detail'),
    path('word_prayer', views.word_prayer, name='word_prayer'),
    path('word_prayer/<int:id>', views.word_prayer_detail, name='word_prayer_detail'),
    path('video_messages', views.video_messages, name='video_messages'),

    path('contact_us', views.contact_us, name='contact_us'),
    path('couple_meeting', views.couple_meeting, name='couple_meeting'),
    path('kcc', views.kcc, name='kcc'),
    path('kcc/<int:id>', views.kcc_detail, name='kcc_detail'),
    path('streaming', views.streaming, name='streaming'),
    path('watchlive', views.watchlive, name='watchlive'),
    path('<int:id>', views.audio_streaming_detail, name='audio_streaming_detail'),
    path('listenlive', views.listenlive, name='listenlive'),
]
