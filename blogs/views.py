from django.shortcuts import render
from .models import Blog

# Create your views here.
def blogs(request):
    blog_data = Blog.objects.order_by('-created_date')
    data = {
    'blog_data': blog_data,
    }
    return render(request, 'blogs/blogs.html', data)
