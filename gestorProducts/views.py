from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from gestorProducts.models import *
from gestorProducts.forms import *
from django.contrib import messages

# Create your views here.

# Vista de Productos
@login_required
def Productos(request):
    producto = Producto.objects.all()
    data = {
        'productos' : producto,
    }
    return render(request, 'mayoristaEconomica/producto.html', data)
@login_required
def insertProductos(request):
    if request.method == 'POST':
        form = ProductoFormRegistration(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('productos'))

    else:
        form = ProductoFormRegistration()

    data = {
        'form': form,
        'title': 'Registrar Producto'
    }

    return render(request, 'mayoristaEconomica/insertComponents.html', data)

@login_required
def editarProductos(request, id):
    producto = Producto.objects.get(id=id)
    form = ProductoFormRegistration(instance=producto)
    if request.method == 'POST':
        form = ProductoFormRegistration(request.POST, instance=producto)
        if form.is_valid():
            print("El form es valido")
            form.save()
            return HttpResponseRedirect(reverse('productos'))
        else:
            print("Hay errores: ", form.errors)
    data = {
        'form': form,
        'title': 'Editar Productos'
    }
    return render(request, 'mayoristaEconomica/insertComponents.html', data)
@login_required
def eliminarProductos(request, id):
    if request.user.is_superuser:
        producto = Producto.objects.get(id = id)
        if producto.cantidad == 0:
            producto.delete()
            messages.success(request, 'El producto se eliminó correctamente.')
        else:
            messages.error(request, 'No se puede eliminar el producto. La cantidad no es 0.')
        return HttpResponseRedirect(reverse('productos'))
    else:
        return render(request, 'mayoristaEconomica/dashboard.html')
    
# Vista de Categorias:

@login_required
def Categoria(request):
    if request.user.is_superuser:
        producto = Categorias.objects.all()
        data = {
            'productos' : producto,
        }
        return render(request, 'mayoristaEconomica/categoria.html', data)
    else:
        return render(request, 'mayoristaEconomica/dashboard.html')
    
@login_required
def insertCategorias(request):
    if request.method == 'POST':
        form = CategoriaFormRegistration(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('categorias'))

    else:
        form = CategoriaFormRegistration()

    data = {
        'form': form,
        'title': 'Registrar Categoria'
    }

    return render(request, 'mayoristaEconomica/insertComponents.html', data)
    
@login_required
def editarCategoria(request, id):
    categorias = Categorias.objects.get(id=id)
    form = CategoriaFormRegistration(instance=categorias)
    if request.method == 'POST':
        form = CategoriaFormRegistration(request.POST, instance=categorias)
        if form.is_valid():
            print("El form es valido")
            form.save()
            return HttpResponseRedirect(reverse('categorias'))
        else:
            print("Hay errores: ", form.errors)
    data = {
        'form': form,
        'title': 'Editar Categoria'
    }
    return render(request, 'mayoristaEconomica/insertComponents.html', data)

@login_required
def eliminarCategoria(request, id):
    if request.user.is_superuser:
        producto = Categorias.objects.get(id = id)
        producto.delete()
        return HttpResponseRedirect(reverse('categorias'))
    else:
        return render(request, 'mayoristaEconomica/dashboard.html')
    
@login_required 
def historyMedia(request):
    return render(request, 'mayoristaEconomica/historialMovimientos.html')

@login_required 
def historyMediaProductos(request):
    historial_cambios = Producto.history.all()
    data = {
        'historial_cambios': historial_cambios
    }
    return render(request, 'mayoristaEconomica/all_historyProducts.html', data)

@login_required 
def historyMediaCategorias(request):
    historial_cambios = Categorias.history.all()
    data = {
        'historial_cambios': historial_cambios
    }
    return render(request, 'mayoristaEconomica/all_historyCategorias.html', data)