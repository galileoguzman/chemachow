from django.template import Context, loader
from django.http import HttpResponse

def hola(request):
	cadenita = "Hola Master Galito :D"
	return HttpResponse(cadenita)

