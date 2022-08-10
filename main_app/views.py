from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Wine


class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def wines_index(request):
  wines = Wine.objects.filter(user=request.user)
  return render(request, 'wines/index.html', { 'wines': wines })

@login_required
def wines_detail(request, wine_id):
  wine = Wine.objects.get(id=wine_id)
  return render(request, 'wines/detail.html', { 'wine': wine })

class WineCreate(LoginRequiredMixin, CreateView):
  model = Wine
  fields = ['name', 'taste', 'year']
  success_url = '/wines/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class WineUpdate(LoginRequiredMixin, UpdateView):
  model = Wine
  fields = ['taste', 'year']
  success_url = '/wines/'

class WineDelete(LoginRequiredMixin, DeleteView):
  model = Wine
  success_url = '/wines/'


def signup(request):
  error_message = ""
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('wines_index')
    else:
      error_message = "Invalid sign up - try again"
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)