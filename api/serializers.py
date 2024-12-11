from rest_framework import serializers
from .models import Articulo, Venta, Ingreso, DetalleIngreso, DetalleVenta

class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Articulo
        fields = ['id', 'nombre', 'stock']

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['id', 'fecha', 'total']

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingreso
        fields = ['id', 'fecha', 'total']

class DetalleIngresoSerializer(serializers.ModelSerializer):
    articulo = ArticuloSerializer()

    class Meta:
        model = DetalleIngreso
        fields = ['id', 'ingreso', 'articulo', 'cantidad', 'precio_unitario']

class DetalleVentaSerializer(serializers.ModelSerializer):
    articulo = ArticuloSerializer()

    class Meta:
        model = DetalleVenta
        fields = ['id', 'venta', 'articulo', 'cantidad', 'precio_unitario']
