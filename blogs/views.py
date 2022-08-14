from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def blogs(request):
    blog_data = Blog.objects.order_by('-created_date')
    paginator = Paginator(blog_data, 9)
    page = request.GET.get('page')
    paged_blog = paginator.get_page(page)

    data = {
    'blog_data': paged_blog,
    }
    return render(request, 'blogs/blogs.html', data)

def blog_detail(request, id):
    blog_detail = get_object_or_404(Blog, pk=id)
    data = {
    'blog_detail': blog_detail,
    }
    return render(request, 'blogs/blog_detail.html', data)
