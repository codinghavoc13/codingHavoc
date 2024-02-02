from django.shortcuts import render

from .models import BlogEntry

# Create your views here.

def blog_main(request):
    blogs = BlogEntry.objects.all()
    return render(request,"projectBlog/index.html",{'blogs':blogs})