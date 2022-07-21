from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView, CreateView, FormView

from pasteleria.forms import LoginForm, UsuarioForm
from .models import User, Cliente

# Create your views here.
def index_view(request):
    return render(request, 'pasteleria/index.html')

#------------------------------------------------------
#       USUARIO 
#------------------------------------------------------
def registro_usuario_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                try:
                    user = User.objects.create_user(
                        username=request.POST['usuario'],
                        email=request.POST['email'],
                        password=request.POST['contraseña'],
                        first_name=request.POST['nombre'],
                        last_name=request.POST['apellidos'],
                        dni = request.POST['dni'],
                        telefono = request.POST['telefono'],
                        direccion = request.POST['direccion'],
                    )
                    Cliente(usuario = user).save()
                    return redirect('login')
                except Exception as e:
                    print(e)
                    messages.error(request, 'Usuario ya existe!')
        else:
            messages.warning(request, 'Ocurrio un problema')
    else:
        form = UsuarioForm()

    return render(request, 'usuario/registro.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            usuario = form.cleaned_data['usuario']
            contraseña = form.cleaned_data['contraseña']

            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                print('Login exitoso')
                login(request, user)
                return redirect('pasteleria:index')
    else:
        form = LoginForm()
    
    return render(request, 'usuario/login.html',{'form':form})




