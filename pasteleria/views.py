from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
#------------------------------------------------------
#       USUARIO 
#------------------------------------------------------
class RegistrarUsuarioView(TemplateView):
    template_name = 'usuario/registro.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class InitiaView(TemplateView):
    template_name = 'usuario/login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
