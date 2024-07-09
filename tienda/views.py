from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Artista, Obra, Carrito_de_Compra, Producto_Carrito
from .forms import DireccionForm

def crud_artista(request):
    if request.POST:
        if "obra_id" in request.POST:
            print("La obra a editar es:", request.POST['obra_id'])

        if "artista_id" in request.POST:
            print("La autor a editar es:", request.POST['artista_id'])
            artista_id = request.POST['artista_id']
            artista = Artista.objects.get(id=artista_id)
            
            if 'Editar_artista' in request.POST:
                print("Lo vamos a editar", artista)
            if 'Eliminar_artista' in request.POST:
                print("Lo vamos a eliminar", artista)
    
    carrito = request.user.carritos.filter(estado="pendiente").first()
    artistas = Artista.objects.all()
    return render(request, 'tienda/crud_artista.html', {'artistas': artistas, 'carrito': carrito})

def CarritoCompras(request):
    context = {}
    return render(request, 'tienda/Carrito_Compras.html', context)

@login_required
def carrito_view(request):
    carrito, created = Carrito_de_Compra.objects.get_or_create(usuario=request.user, estado='pendiente')
    # Calcular el total del carrito
    carrito.total = sum(item.productos.precio * item.cantidad for item in carrito.productos.all())
    carrito.save()
    obras = Obra.objects.all()  # Asegúrate de pasar las obras disponibles al contexto
    return render(request, 'tienda/carrito.html', {'carrito': carrito, 'obras': obras})

@login_required
def agregar_al_carrito(request, obra_id):
    obra = get_object_or_404(Obra, id=obra_id)
    carrito, created = Carrito_de_Compra.objects.get_or_create(usuario=request.user, estado='pendiente')
    
    # Verificar si el producto ya está en el carrito
    producto_carrito, created = Producto_Carrito.objects.get_or_create(productos=obra, carrito=carrito)
    
    if not created:
        # Si el producto ya está en el carrito, aumentar la cantidad
        producto_carrito.cantidad += 1
    else:
        # Si es un nuevo producto en el carrito, establecer la cantidad en 1
        producto_carrito.cantidad = 1
    
    producto_carrito.save()
    # Calcular el total del carrito
    carrito.total = sum(item.productos.precio * item.cantidad for item in carrito.productos.all())
    carrito.save()
    return redirect('carrito')

@login_required
def remove_from_cart(request):
    if request.method == 'POST':
        obra_id = request.POST.get('obra_id')
        carrito = Carrito_de_Compra.objects.get(usuario=request.user, estado='pendiente')
        producto = get_object_or_404(Producto_Carrito, productos_id=obra_id, carrito=carrito)
        producto.delete()
        # Calcular el total del carrito
        carrito.total = sum(item.productos.precio * item.cantidad for item in carrito.productos.all())
        carrito.save()
        return redirect('carrito')

@login_required
def clear_cart(request):
    carrito = Carrito_de_Compra.objects.get(usuario=request.user, estado='pendiente')
    carrito.productos.all().delete()
    carrito.total = 0
    carrito.save()
    return redirect('carrito')

def añadir_direccion(request):
    form = DireccionForm()
    if request.method == 'POST':
        form = DireccionForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'tienda/añadir_direccion.html', {'form': form})

def realizar_pago(request):
    carrito = Carrito_de_Compra.objects.get(usuario=request.user, estado='pendiente')
    carrito.estado = 'comprado'
    carrito.save()
    return render(request, 'compra.html', {'carrito': carrito})