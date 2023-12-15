from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)