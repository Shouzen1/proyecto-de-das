from django.shortcuts import render
from django.http import JsonResponse
import json

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
	carrito = request.user.carritos.filter(estado="pendiente")
	if len(carrito)>0:
		carrito=carrito[0]
	else:
		carrito=None

	artistas = Artista.objects.all()
	return render(request, 'tienda/crud_artista.html', {'artistas': artistas, 'carrito':carrito})

def CarritoCompras(request):
    context={}
    return render(request, 'tienda\Carrito_Compras.html',context)

def carrito_view(request):
    obras = Obra.objects.all()
    return render(request, 'tienda/carrito.html', {'obras': obras})

def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        obra_id = data.get('obra_id')
        obra = Obra.objects.get(id=obra_id)
        cart = request.session.get('cart', [])
        cart.append({
            'id': obra.id,
            'nombre': obra.nombre,
            'precio': obra.precio,
        })
        request.session['cart'] = cart
        return JsonResponse({'success': True, 'cart': cart})
    return JsonResponse({'success': False})

def remove_from_cart(request):
    # Lógica para eliminar un artículo del carrito
    if request.method == 'POST':
        obra_id = request.POST.get('obra_id')
        # Realiza la lógica necesaria para eliminar el artículo del carrito

        # Actualiza el carrito en la sesión u otra estructura de datos
        cart = []

        # Puedes realizar otras operaciones necesarias aquí, como actualizar el total del carrito, etc.

        response_data = {
            'success': True,
            'cart': cart,
            'total_amount': 0.0  # Actualiza el total si es necesario
        }
        return JsonResponse(response_data)

def clear_cart(request):
    cart = []
    total_amount = 0.0
    
    response_data = {
        'success': True,
        'cart': cart,
        'total_amount': total_amount
    }
    return JsonResponse(response_data)


