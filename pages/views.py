from django.shortcuts import render
from blogs.models import Blog, Audio_msg


# Create your views here.
def home(request):
    blog_data = Blog.objects.order_by('-created_date')
    data = {
    'blog_data': blog_data,
    }
    return render(request, 'pages/home.html', data)


def blog(request):
    return render(request, 'pages/blog.html')


def audio_messages(request):
    return render(request, 'pages/audio_messages.html')

def imgc(request):
    blog_data = Blog.objects.order_by('-created_date').filter(category='IMGC')
    data = {
    'blog_data': blog_data,
    }
    return render(request, 'pages/imgc.html', data)

def tsc(request):
    blog_data = Blog.objects.order_by('-created_date').filter(category='TSC')
    data = {
    'blog_data': blog_data,
    }
    return render(request, 'pages/tsc.html', data)


def word_prayer(request):
    blog_data = Blog.objects.order_by('-created_date').filter(category='WAP')
    data = {
    'blog_data': blog_data,
    }
    return render(request, 'pages/word_prayer.html', data)

def video_messages(request):
    return render(request, 'pages/video_messages.html')


def audio_messages(request):
    return render(request, 'pages/audio_messages.html')


def contact_us(request):
    return render(request, 'pages/contact_us.html')

def couple_meeting(request):
    return render(request, 'pages/couple_meeting.html')

def kcc(request):
    blog_data = Blog.objects.order_by('-created_date').filter(category='KCC')
    data = {
    'blog_data': blog_data,
    }
    return render(request, 'pages/kcc.html', data)


def streaming(request):
    return render(request, 'pages/streaming.html')

def video_streaming(request):
    return render(request, 'pages/audio_streaming.html')

def audio_streaming(request):
    return render(request, 'pages/video_streaming.html')

def audio_msg(request):
    audio_data = Audio_msg.objects.order_by('-created_date')
    data = {
    'audio_data': audio_data,
    }
    return render(request, 'pages/audio_msg.html', data)
