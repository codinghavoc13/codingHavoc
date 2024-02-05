from django.shortcuts import render

from .models import BlogEntry

# Create your views here.

def blog_main(request):
    blogs, recent_blogs, blog_date_groups = get_blogs('ALL')
    
    return render(request,"project_blog/index.html",
                  {'blogs':blogs,
                   'blog_date_groups':blog_date_groups,
                   'recent_blogs': recent_blogs})

def show_filter(request, filter):
    blogs, recent_blogs, blog_date_groups = get_blogs(filter)
    return render(request,"project_blog/index.html",
                  {'blogs':blogs,
                   'blog_date_groups':blog_date_groups,
                   'recent_blogs': recent_blogs})

def get_blogs(filter):
    temp_blogs = BlogEntry.objects.all().order_by('-postDate')
    recent_blogs = []
    blogs = []
    blog_date_groups = []
    for blog in temp_blogs:
        if recent_blogs.__len__() < 3:
            recent_blogs.append(blog)
        date_group = blog.postDate.strftime("%B-%Y")
        if date_group not in blog_date_groups:
            blog_date_groups.append(date_group)
        if filter != 'ALL':
            args = filter.split('-')
            date_check = date_group.split('-')
            if date_check[0] == args[0] and date_check[1]==args[1]:
                blogs.append(blog)
        else:
            blogs.append(blog)
    return blogs, recent_blogs, blog_date_groups