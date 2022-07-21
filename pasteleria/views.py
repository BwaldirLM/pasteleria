from django.contrib import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.db import transaction
from django.views.generic import TemplateView, CreateView, FormView

from pasteleria.forms import UsuarioForm
from .models import User, Cliente

# Create your views here.
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


class InitiaView(TemplateView):
    template_name = 'usuario/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
