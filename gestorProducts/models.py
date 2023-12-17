from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categorias(models.Model):
    codigo = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=99)
    descripcion = models.CharField(max_length=99)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.IntegerField(unique=True)
    cantidad = models.IntegerField()
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.CharField(max_length=99)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Compra(models.Model):
    numeroCompra = models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=50)
    total = models.IntegerField()
    fecha = models.DateField()

class CompraProductos(models.Model):
    idProducto = models.ForeignKey(Producto, on_delete=models.CASCADE)      
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)

class Proveedor(models.Model):
    nombre = models.CharField(max_length=99)
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=90)

class Pagos(models.Model):
    fecha = models.DateField()
    monto = models.IntegerField()
    estado = models.CharField(max_length=50)

class CompraPagos(models.Model):
    idCompra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    idPagos = models.ForeignKey(Pagos, on_delete=models.CASCADE)

class Cliente(models.Model):
    rut = models.IntegerField(unique=True)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=50)

class Cajero(models.Model):
    numeroCajero = models.IntegerField()
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)

class Venta(models.Model):
    tipoDeDocumento = models.CharField(max_length=50)
    idCliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    idCajero = models.ForeignKey(Cajero, on_delete=models.CASCADE)

class FormaPagosVenta(models.Model):
    idPagos = models.ForeignKey(Pagos, on_delete=models.CASCADE)
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)

class DetalleVenta(models.Model):
    codigoVenta = models.CharField(max_length=50, unique=True)
    fecha = models.DateField()
    precios = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField()
    metodoPago = models.CharField(max_length=50)
    idVenta = models.ForeignKey(Venta, on_delete=models.CASCADE)