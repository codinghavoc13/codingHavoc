from django.db import models

# Create your models here.
#rewrite this to use underscores instead of camelcasing
class BlogEntry(models.Model):
    postDate = models.DateField()
    postTitle = models.CharField(max_length=150)
    postText = models.TextField()