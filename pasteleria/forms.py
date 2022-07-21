from socket import fromshare
from django import forms

from pasteleria.models import Cliente, User

#-----------------------------------
#       USUARIO
#-----------------------------------
class UsuarioForm(forms.Form):
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Usuario'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Nombres'}))
    apellidos = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Apellidos'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email'}))
    contraseña = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Contraseña'}))  
    dni = forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'DNI'}))
    telefono=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Telefono'}))
    direccion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Direccion'}))

    def is_valid(self):
        valid = super(UsuarioForm, self).is_valid()
        if valid:
            
            return True
        else:             
            for error in self.errors:
                self.fields[error].widget.attrs.update({'class':'form-control is-invalid'})
                       
            return False
    
    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            if User.objects.get(email=email):
                raise forms.ValidationError('Este correo ya esta registrado')
        except User.DoesNotExist:
            return email

    def clean_matricula(self):
        dni = self.cleaned_data['dni']
        try:
            if Cliente.objects.get(dni=dni):
                raise forms.ValidationError('Este DNI ya fue registrado')
        except Cliente.DoesNotExist:
            return dni