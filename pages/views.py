from django.shortcuts import render, get_object_or_404
from blogs.models import Blog
from audio_msg.models import Audio_msg
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


# Create your views here.
def home(request):
    blog_data = Blog.objects.order_by('-created_date')
    audio_data = Audio_msg.objects.order_by('-created_date')
    data = {
    'blog_data': blog_data,
    'audio_data': audio_data,
    }
    return render(request, 'pages/home.html', data)


def blog(request):
    return render(request, 'pages/blog.html')


def audio_messages(request):
    return render(request, 'pages/audio_messages.html')

def imgc(request):
    blog_data = Blog.objects.order_by('-created_date').filter(category='IMGC')
    paginator = Paginator(blog_data, 9)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    data = {
    'blog_data': paged_blog,
    }
    return render(request, 'pages/imgc.html', data)

def imgc_detail(request, id):
    blog_detail = get_object_or_404(Blog, pk=id)
    data = {
    'blog_detail': blog_detail,
    }
    return render(request, 'pages/imgc_detail.html', data)

def tsc(request):
    blog_data = Blog.objects.order_by('-created_date').filter(category='TSC')

    paginator = Paginator(blog_data, 9)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
    data = {
    'blog_data': paged_blog,
    }
    return render(request, 'pages/tsc.html', data)

def tsc_detail(request, id):
    blog_detail = get_object_or_404(Blog, pk=id)
    data = {
    'blog_detail': blog_detail,
    }
    return render(request, 'pages/tsc_detail.html', data)

def word_prayer(request):
    blog_data = Blog.objects.order_by('-created_date').filter(category='WAP')
    paginator = Paginator(blog_data, 9)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)
 
    data = {
    'blog_data': paged_blog,
    }
    return render(request, 'pages/word_prayer.html', data)

def word_prayer_detail(request, id):
    blog_detail = get_object_or_404(Blog, pk=id)
    data = {
    'blog_detail': blog_detail,
    }
    return render(request, 'pages/word_prayer_detail.html', data)

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

def kcc_detail(request, id):
    blog_detail = get_object_or_404(Blog, pk=id)
    data = {
    'blog_detail': blog_detail,
    }
    return render(request, 'pages/kcc_detail.html', data)

def streaming(request):
    return render(request, 'pages/streaming.html')

def watchlive(request):
    return render(request, 'pages/watchlive.html')

def listenlive(request):
    return render(request, 'pages/listenlive.html')

def audio_msg(request):
    audio_data = Audio_msg.objects.order_by('-created_date')

    data = {
    'audio_data': audio_data,

    }
    return render(request, 'pages/audio_msg.html', data)

def audio_streaming_detail(request, id):
    audio_data = get_object_or_404(Audio_msg, pk=id)
    data = {
    'audio_data': audio_data,
    }
    return render(request, 'pages/audio_streaming_detail.html', data)
