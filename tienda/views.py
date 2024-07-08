from django.shortcuts import render

# Create your views here.
from .models import *

def crud_artista(request):

	if request.POST:
		print("POST")
		if "obra_id" in request.POST:
			print("La obra a editar es:", request.POST['obra_id'])



		if "artista_id" in request.POST:
			print("La autor a editar es:", request.POST['artista_id'])
			artista_id = request.POST['artista_id']
			artista = Artista.objects.get(id=artista_id)
			
			if 'Editar_artista' in request.POST:
				print("Lo vamos a editar",artista)
			if 'Eliminar_artista' in request.POST:
				print("Lo vamos a eliminar",artista)

	artistas = Artista.objects.all()
	return render(request, 'tienda/crud_artista.html', {'artistas': artistas})