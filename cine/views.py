from django.shortcuts import render
from django.utils import timezone
from .models import Director, Peliculas
from cine.models import Director
from cine.models import Peliculas


def peliculas_list(request):
    pelis = Peliculas.objects.all()
    return render(request, 'cine/peliculas_list.html', {'pelis': pelis})


