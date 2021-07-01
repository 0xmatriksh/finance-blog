from django.shortcuts import render
from .models import Blog

# Create your views here.


def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request, 'website/home.html',context)

def detail(request,slug):
    blog = Blog.objects.all().get(slug=slug) 
    print(blog.image.url)
    context = {
        'blog' : blog
    }
    return render(request, 'website/blog_detail.html',context)
