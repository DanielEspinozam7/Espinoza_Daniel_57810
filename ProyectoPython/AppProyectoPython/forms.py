from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    correo = forms.CharField(max_length=50, required=True)
    telefono = forms.IntegerField(required=True)
    
class CotizacionForm(forms.Form):
    detalle = forms.CharField(max_length=5000, required=True)
    mayorista = forms.CharField(max_length=50, required=True)
    

class ProductoForm(forms.Form):
    nombreProducto = forms.CharField(max_length=200, required=True)
    marca = forms.CharField(max_length=50, required=True)
    stock = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)
    url = forms.CharField(max_length=200, required=True)
    
class RegistroForm(UserCreationForm):
    email = forms.EmailField(required = True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {"username", "password1", "password2", "email"}
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="Nombre", max_length=50, required=True)
    last_name = forms.CharField(label="Apellido", max_length=50, required=True)
    
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        
class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)