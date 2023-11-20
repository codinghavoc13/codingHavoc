from django.shortcuts import render
import json
import numpy
import os

def home(request):
    print("Checking for CI")
    if "PROD_ENV" in os.environ:
        print("HEROKU")
    else:
        print("LOCAL")
    data = open('main/static/main/data.json')
    data1 = data.read()
    data2 = json.loads(data1)
    
    hobbies = randomiseHobbies(data2['hobbyInterests'])
    return render(request,"main/index.html",{'linkResults':data2['linkList'],'hobbyList0':hobbies[0],'hobbyList1':hobbies[1],'hobbyList2':hobbies[2]})

def about(request):
    return render(request,"main/about.html")

def projects(request):
    return render(request, "main/projects.html")

def randomiseHobbies(arr):
    numpy.random.shuffle(arr)
    result = numpy.array_split(arr,3)
    return result