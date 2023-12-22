from django import forms

from .passwordUtil import hash_password

from .models import User

class RegistrationForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    userName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def prepUser(self):
        result = None
        f = self.cleaned_data.get('firstName')
        l = self.cleaned_data.get('lastName')
        u = self.cleaned_data.get('userName')
        p = self.cleaned_data.get('password')
        #add check later to check for existing user with same username
        if User.objects.filter(userName=u).exists():
            raise forms.ValidationError('User name "{u}" is already in use')

        hashSet = hash_password(p)
        salt, b64_hash = hashSet.split("$", 1)
        result = User.objects.create(firstName = f, lastName = l, userName = u, passHash = b64_hash, passSalt = salt)
        return result

class LoginForm(forms.Form):
    userName = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def prepUser(self):
        result = {}
        result['userName'] = self.cleaned_data.get('userName')
        result['password'] = self.cleaned_data.get('password')
        return result