from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=250)
  slug = models.SlugField()
  date_posted = models.DateTimeField(default=datetime.utcnow)
  body = models.TextField()

  def __str__(self):
    return self.title