from django.db import models

class Articulo(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Venta {self.id} - {self.fecha}"

class Ingreso(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Ingreso {self.id} - {self.fecha}"

class DetalleIngreso(models.Model):
    ingreso = models.ForeignKey(Ingreso, related_name='detalles', on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, related_name='detalles_ingreso', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.articulo.nombre} - {self.cantidad}"

class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, related_name='detalles', on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, related_name='detalles_venta', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.articulo.nombre} - {self.cantidad}"
