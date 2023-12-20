from django.db import models

from .passwordUtil import hash_password

class User(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    passHash = models.CharField(max_length=150)
    passSalt = models.CharField(max_length=150)
    userName = models.CharField(max_length=50)