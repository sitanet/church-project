from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'pages/home.html')


def blog(request):
    return render(request, 'pages/blog.html')


def audio_messages(request):
    return render(request, 'pages/audio_messages.html')

def imgc(request):
    return render(request, 'pages/imgc.html')

def tsc(request):
    return render(request, 'pages/tsc.html')


def word_prayer(request):
    return render(request, 'pages/word_prayer.html')

def video_messages(request):
    return render(request, 'pages/video_messages.html')


def audio_messages(request):
    return render(request, 'pages/audio_messages.html')


def contact_us(request):
    return render(request, 'pages/contact_us.html')

def couple_meeting(request):
    return render(request, 'pages/couple_meeting.html')

def kcc(request):
    return render(request, 'pages/kcc.html')


def streaming(request):
    return render(request, 'pages/streaming.html')
