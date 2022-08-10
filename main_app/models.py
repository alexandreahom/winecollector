from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Wine(models.Model):
  name = models.CharField(max_length=100)
  taste = models.TextField(max_length=250)
  year = models.IntegerField()
  user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('wines_detail', kwargs={'wine_id': self.id})