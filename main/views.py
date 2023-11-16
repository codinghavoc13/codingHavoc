from django.shortcuts import render
import json

linkList = [
    {
        "site": "https://www.linkedin.com/in/sean-hayes-1a609888/",
        "icon": "/main/image/linkedin.511x512.png",
        "altText":"LinkedIn Profile",
        "randomText": "A"
    },{
        "site": "https://github.com/seanhayes13/dev",
        "icon": "main/image/github-6980894_640.png",
        "altText":"GitHub Dev Repo",
        "randomText": "B"
    },{
        "site": "https://www.hackerrank.com/profile/seanhayes13",
        "icon": "main/image/600px-HackerRank_Icon-1000px.png",
        "altText":"HackerRank Profile",
        "randomText": "C"
    }
]

def home(request):
    return render(request,"main/index.html")

def about(request):
    return render(request,"main/about.html")

def links(request):
    return render(request,"main/links.html",{'linkResults':linkList})

def contact(request):
    return render(request,"main/contact.html")

def hobbies(request):
    return render(request,"main/hobbies.html")

def projects(request):
    return render(request, "main/projects.html")