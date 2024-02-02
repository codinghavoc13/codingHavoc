from django.db import models

# Create your models here.
class BlogEntry(models.Model):
    postDate = models.DateField()
    postTitle = models.CharField(max_length=150)
    postText = models.TextField()