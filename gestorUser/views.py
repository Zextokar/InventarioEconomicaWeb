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
    producto = User.objects.all()
    data = {
        'productos' : producto,
    }
    return render(request, 'mayoristaEconomica/usergestion.html', data)

@login_required
def InsertUser(request):
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

@login_required
def editUser(request, id):
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

@login_required
def deleteUser(request, id):
    if request.user.is_superuser:
        producto = User.objects.get(id = id)
        producto.delete()
        return HttpResponseRedirect(reverse('usergestion'))
    else:
        return render(request, 'mayoristaEconomica/dashboard.html')
    
@login_required
def SectionVentas(request):
    return render(request, 'mayoristaEconomica/sectionVentas.html')

def UserInfo(request):
    # Asegúrate de que el usuario esté autenticado antes de intentar obtener sus datos personales
    if request.user.is_authenticated:
        # Obtén el objeto DatosPersonales asociado al usuario actual
        datos_personales = DatosPersonales.objects.get(user=request.user)

        data = {
            'datos_personales': datos_personales
        }

        return render(request, 'mayoristaEconomica/userInfo.html', data)
    else:
        # Manejar el caso en el que el usuario no esté autenticado
        return render(request, 'mayoristaEconomica/userInfo.html', {})