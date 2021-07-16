from django.shortcuts import render,redirect
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .models import Blog
from asgiref.sync import sync_to_async
from django.db.models import Q
import requests
import httpx

def home(request):
    if request.method == "POST":
        data = request.POST['name_blog']
        queries = data.split(" ")
        for q in queries:
            objects = Blog.objects.filter(
                Q(title__icontains=q) |
                Q(content__icontains=q)
            ).order_by('-created_at')
    else:
        objects = Blog.objects.all().order_by('-created_at')
    paginator = Paginator(objects,6)
    number = request.GET.get('page')
    try:
        blogs = paginator.get_page(number)
    except PageNotAnInteger:
        blogs = paginator.get_page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    context = {
        'blogs':blogs
    }
    return render(request, 'website/home.html',context)

def detail(request,slug):
    blog = Blog.objects.all().get(slug=slug) 
    context = {
        'blog' : blog
    }
    return render(request, 'website/blog_detail.html',context)


@sync_to_async
def nepse(request):
    r = httpx.get('https://newweb.nepalstock.com.np/api/nots/nepse-index').json()
    data = r[3]
    context = {
        'data':data
    }
    return render(request,'website/nepse.html',context)
    


