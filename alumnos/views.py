from django.shortcuts import render, redirect
from .models import ObraDeArte
from .forms import ObraDeArteForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


# Create your views here.

def index(request):
    context={}
    return render(request, 'alumnos/1.html',context)

def account(request):
    context={}
    return render(request, 'alumnos/login.html',context)

def carrito(request):
    context={}
    return render(request, 'alumnos/carrito.html',context)

def htedgnf(request):
    context={}
    return render(request, 'alumnos/htedgnf.html',context)

def frida(request):
    context={}
    return render(request, 'alumnos/frida.html',context)

def nosotros(request):
    context={}
    return render(request, 'alumnos/nosotros.html',context)

def miguel(request):
    context={}
    return render(request, 'alumnos/miguelangel.html',context)

def vincent(request):
    context={}
    return render(request, 'alumnos/VincentvanGogh.html',context)

@login_required
def añadir_arte(request):
    if request.method == 'POST':
        form = ObraDeArteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumnos:listar_arte')
    else:
        form = ObraDeArteForm()
    return render(request, 'alumnos/AñadirArte.html', {'form': form})

@login_required
def listar_arte(request):
    obras = ObraDeArte.objects.all()
    return render(request, 'alumnos/ListarArte.html', {'obras': obras})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            return redirect('alumnos:index')
    else:
        form = UserCreationForm()

    context = {
        'form': form,
    }
    return render(request, 'alumnos/registro.html', context)


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('alumnos:listar_arte')
        else:
            error_message = 'Usuario o contraseña incorrectos'
            return redirect('alumnos:index')
    else:
        return render(request, 'login.html')
