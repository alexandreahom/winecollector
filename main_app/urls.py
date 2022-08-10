from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('wines/', views.wines_index, name='wines_index'),
  path('wines/<int:wine_id>/', views.wines_detail, name='wines_detail'),
  path('wines/create/', views.WineCreate.as_view(), name='wines_create'),
  path('wines/<int:pk>/update/', views.WineUpdate.as_view(), name='wines_update'),
  path('wines/<int:pk>/delete/', views.WineDelete.as_view(), name='wines_delete'),
]