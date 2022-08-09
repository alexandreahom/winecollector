from django.db import models
from django.urls import reverse

class Wine(models.Model):
  name = models.CharField(max_length=100)
  brand = models.CharField(max_length=100)
  taste = models.TextField(max_length=250)
  year = models.IntegerField()

def __str__(self):
    return self.name

def get_absolute_url(self):
    return reverse('wines_detail', kwargs={'wine_id': self.id})