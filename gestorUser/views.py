from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from gestorUser.forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from gestorUser.models import *

# Create your views here.
@login_required
def Dashboard(request):
    return render(request, 'mayoristaEconomica/dashboard.html')

# Vista Usuarios
@login_required
def Usergestion(request):
    if request.user.is_superuser:
        producto = User.objects.all()
        data = {
            'productos': producto,
        }
        return render(request, 'mayoristaEconomica/usergestion.html', data)
    else:
        return render(request, 'mayoristaEconomica/dashboard.html')


@login_required
def InsertUser(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = UsuarioFormRegistration(request.POST)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.save()
                return HttpResponseRedirect(reverse('usergestion'))
        else:
            form = UsuarioFormRegistration()

        data = {
            'form': form,
            'title': 'Registrar Usuarios'
        }

        return render(request, 'mayoristaEconomica/insertComponents.html', data)
    else:
        return render(request, 'mayoristaEconomica/dashboard.html')


@login_required
def editUser(request, id):
    if request.user.is_superuser:
        categorias = User.objects.get(id=id)
        form = UsuarioFormRegistration(instance=categorias)
        if request.method == 'POST':
            form = UsuarioFormRegistration(request.POST, instance=categorias)
            if form.is_valid():
                print("El form es valido")
                form.save()
                return HttpResponseRedirect(reverse('usergestion'))
            else:
                print("Hay errores: ", form.errors)
        data = {
            'form': form,
            'title': 'Editar Usuarios'
        }
        return render(request, 'mayoristaEconomica/insertComponents.html', data)
    else:
        return render(request, 'mayoristaEconomica/dashboard.html')

@login_required
def deleteUser(request, id):
    if request.user.is_superuser:
        producto = User.objects.get(id=id)
        producto.delete()
        return HttpResponseRedirect(reverse('usergestion'))
    else:
        return render(request, 'mayoristaEconomica/dashboard.html')
    
@login_required
def SectionVentas(request):
    return render(request, 'mayoristaEconomica/sectionVentas.html')


@login_required
def UserInfo(request):
    if request.user.is_authenticated:
        datos_personales = DatosPersonales.objects.get(user=request.user)

        data = {
            'datos_personales': datos_personales
        }

        return render(request, 'mayoristaEconomica/userInfo.html', data)
    else:
        return render(request, 'mayoristaEconomica/userInfo.html', {})