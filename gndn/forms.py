from django import forms
from django.db import IntegrityError

from .passwordUtil import hash_password

from .models import User

class RegistrationForm(forms.Form):
    firstName = forms.CharField(required=True)
    lastName = forms.CharField(required=True)
    userName = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())

    def prepUser(self):
        result = None
        try:
            f = self.cleaned_data.get('firstName')
            l = self.cleaned_data.get('lastName')
            u = self.cleaned_data.get('userName')
            p = self.cleaned_data.get('password')

            hashSet = hash_password(p)
            salt, b64_hash = hashSet.split("$", 1)
            result = User.objects.create(firstName = f, lastName = l, userName = u, passHash = b64_hash, passSalt = salt)
            return result
        except IntegrityError as e:
            self.add_error('userName', forms.ValidationError('User name is already in use'))
            return result
        

class LoginForm(forms.Form):
    userName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def prepUser(self):
        result = {}
        result['userName'] = self.cleaned_data.get('userName')
        result['password'] = self.cleaned_data.get('password')
        return result