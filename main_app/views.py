from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Wine

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def wines_index(request):
  wines = Wine.objects.all()
  return render(request, 'wines/index.html', { 'wines': wines })

def wines_detail(request, wine_id):
  wine = Wine.objects.get(id=wine_id)
  return render(request, 'wines/detail.html', { 'wine': wine })

class WineCreate(CreateView):
  model = Wine
  fields = ['name', 'brand', 'taste', 'year']
  success_url = '/wines/'

class WineUpdate(UpdateView):
  model = Wine
  fields = ['breed', 'taste', 'year']

class WineDelete(DeleteView):
  model = Wine
  success_url = '/wines/'