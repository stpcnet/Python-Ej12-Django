#from django.test import TestCase

from cine.models import Director
from cine.models import Peliculas

for j in Peliculas.objects.all():
	print(j)
