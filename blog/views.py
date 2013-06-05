from django.template import Context, loader
from django.http import HttpResponse

def probando(request):
	return HttpResponse('hola');

def inicio(request):
	template_name = loader.get_template('index.html')
	contexto = Context({})
	return HttpResponse(template_name.render(contexto))