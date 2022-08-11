from django.urls import path
from . import views

urlpatterns = [
    path('', views.peliculas_list, name='peliculas_list'),
    ]
