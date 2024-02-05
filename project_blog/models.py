from django.db import models

# Create your models here.
#rewrite this to use underscores instead of camelcasing
class BlogEntry(models.Model):
    post_date = models.DateField()
    post_title = models.CharField(max_length=150)
    post_text = models.TextField()