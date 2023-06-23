from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import  CustomUserCreationForm ,CelularForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib import messages
from .models import Celular


def registro(request):
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            user = formulario.save()
            login(request, user)
            messages.success(request, f"Bienvenido/a: {user.username}, ¡Te has registrado correctamente!")
            return redirect('pagina_principal')
    else:
        formulario = CustomUserCreationForm()

    context = {'form': formulario}
    return render(request, 'registration/login.html', context)

def listarcelular(request): 
    celulares=Celular.objects.all()
    return render(request, '../templates/productos.html', {'celulares':  celulares})

def producto(request): 
    celulares=Celular.objects.all()
    context={"celulares": celulares    }
    return render(request, '../templates/productos.html', context)

class ProductoCreate (CreateView):
    model = Celular
    form_class = CelularForm
    template_name = '../templates/crear.html'
    success_url = reverse_lazy('producto')

class editar(UpdateView):
    model = Celular
    form_class = CelularForm
    template_name = '../templates/editar.html'
    success_url = reverse_lazy('producto')

def borrar(request, pk):
    instancia = Celular.objects.get(id=pk)
    instancia.delete()

    return redirect('producto')

def pagina_principal(request):
    return render(request, '../templates/Principal/index.html')

def crear_cuenta(request):
    return render(request, '../templates/Usuario/crear_cuenta.html')

def productos(request):
    return render(request, '../templates/productos.html')

def acerca(request):
    return render(request, '../templates/acerca.html')

def contacto(request):
    return render(request, '../templates/contacto.html')

def api(request):
    return render(request, '../templates/api.html')

def listado(request):
    return render(request, "templates/lista_productos.html")

def crear(request):
    return render(request, '../templates/crear.html')