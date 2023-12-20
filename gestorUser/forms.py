from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from gestorUser.models import *

class UsuarioFormRegistration(UserCreationForm):
    username = forms.CharField(max_length=99, required=True)
    password1 = forms.CharField(max_length=99, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=99, required=True, widget=forms.PasswordInput)
    is_staff = forms.BooleanField(required=False,initial=False)
    is_superuser = forms.BooleanField(required=False,initial=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'is_staff', 'is_superuser']

    username.widget.attrs['class'] = 'form-control'
    password1.widget.attrs['class'] = 'form-control'
    password2.widget.attrs['class'] = 'form-control'
    is_staff.widget.attrs['class'] = 'form-input'
    is_superuser.widget.attrs['class'] = 'form-input'
    
class UsuarioInfoFormRegistration(forms.Form):
    
    nombre = forms.CharField(max_length=99)
    apellido_paterno = forms.CharField(max_length=99)
    apellido_materno = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=99)
    cargo = forms.CharField(max_length=100)
    
    nombre.widget.attrs['class'] = 'form-control'
    apellido_paterno.widget.attrs['class'] = 'form-control'
    apellido_materno.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    cargo.widget.attrs['class'] = 'form-control'
    
class UsuarioInfoFormRegistration(forms.ModelForm):
    
    nombre = forms.CharField(max_length=99)
    apellido_paterno = forms.CharField(max_length=99)
    apellido_materno = forms.CharField(max_length=100)
    direccion = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=99)
    cargo = forms.CharField(max_length=100)
    
    nombre.widget.attrs['class'] = 'form-control'
    apellido_paterno.widget.attrs['class'] = 'form-control'
    apellido_materno.widget.attrs['class'] = 'form-control'
    direccion.widget.attrs['class'] = 'form-control'
    telefono.widget.attrs['class'] = 'form-control'
    cargo.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = DatosPersonales
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['user'].widget.attrs.update({'class': 'form-control'})