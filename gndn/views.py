from django.db import IntegrityError
from django.forms import ValidationError
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render

from django.conf import settings

from .models import User

from .forms import LoginForm, RegistrationForm

from .passwordUtil import verify_password

def gndn_main(request):
    return render(request, "gndn/index.html")

def gndn_register(request):
    return render(request, "gndn/register.html")

def gndn_login(request):
    context = {
        'login_failed':False
    }
    return render(request, "gndn/login.html",context=context)

def gndn_logged_in(request):
    return render(request, "gndn/loggedin.html")

def register(request):
    print("gndn.views.register")
    new_user = None
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.prepUser()
            if not new_user:
                return render(request,'gndn/register.html', {'form':form})
            else:
                request.session['userName'] = new_user.userName
                context = {
                    'firstName':new_user.firstName,
                    'lastName':new_user.lastName,
                    'userName':new_user.userName,
                    'logged_in_status': True
                }
                return render(request, 'gndn/loggedin.html', context=context)
        else:
            return render(request,'gndn/register.html', {'form':form})
    else:
        return HttpResponseRedirect('gndn/register')

def login(request):
    print("gndn.views.login")
    if request.method =='GET':
        form = LoginForm(request.GET)
        if form.is_valid():
            loginDetails = form.prepUser()
            userDetails = User.objects.get(userName=loginDetails['userName'])
            check = verify_password(loginDetails['password'],userDetails.passHash, userDetails.passSalt)
            if check:
                request.session['userName'] = loginDetails['userName']
                context = {
                    'firstName':userDetails.firstName,
                    'lastName':userDetails.lastName,
                    'userName':userDetails.userName,
                    'logged_in_status': True
                }
                return render(request, 'gndn/loggedin.html', context=context)
            else:
                context = {
                    'login_failed': True
                }
                return render(request,'gndn/login.html', context=context)
        else:
            raise Http404
    else:
        return HttpResponseRedirect('gndn/register')

def logout(request):
    print("gndn.views.logout")
    del request.session['userName']
    context = {
        'logged_in_status': False
    }
    return render(request, 'gndn/index.html',context=context)