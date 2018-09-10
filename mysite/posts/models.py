from django.db import models
from datetime import datetime

# Create your models here.

class Posts (models.Model):
  text = models.TextField(max_length=1000)
  created_at = models.DateTimeField(default=datetime.now, blank=True)
  ip = models.CharField(max_length=20)