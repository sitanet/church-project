from django.shortcuts import render, get_object_or_404
from .models import Audio_msg
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def audio_msg(request):
    audio_data = Audio_msg.objects.order_by('-created_date')
    paginator = Paginator(audio_data, 9)
    page = request.GET.get('page')
    audio_data = paginator.get_page(page)
    data = {
    'audio_data': audio_data,
    }
    return render(request, 'audio/audio_msg.html', data)

def audio_detail(request, id):
    audio_detail = get_object_or_404(Audio_msg, pk=id)
    data = {
    'audio_detail': audio_detail,
    }
    return render(request, 'audio/audio_detail.html', data)
