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
    return render(request, "gndn/login.html")

def gndn_logged_in(request):
    return render(request, "gndn/loggedin.html")

def register(request):
    print("gndn.views.register")
    userName = "WTF"
    new_user = None
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        #need to add a check to see if the username is already taken
        if form.is_valid():
            userName = form.cleaned_data['userName']
            new_user = form.prepUser()
            if not new_user:
                return HttpResponseRedirect('gndn/register')
            else:
                # logged_in = True
                request.session['userName'] = userName
                context = {
                    'firstName':new_user.firstName,
                    'lastName':new_user.lastName,
                    'userName':new_user.userName,
                    'logged_in_status': True
                }
                return render(request, 'gndn/loggedin.html', context=context)
        else:
            # print(form.errors)
            raise Http404            
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