from rest_framework import generics
from .models import Articulo, Venta, Ingreso, DetalleIngreso, DetalleVenta
from .serializers import ArticuloSerializer, VentaSerializer, IngresoSerializer, DetalleIngresoSerializer, DetalleVentaSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la API del Sistema POS")

class ArticuloListCreate(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    
class ArticuloDetail(generics.RetrieveUpdateDestroyAPIView):  # Vista para manejar PUT, GET y DELETE por ID
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer
    lookup_field = 'id'

class VentaListCreate(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    
class VentaDetail(generics.RetrieveUpdateDestroyAPIView):  # Vista para manejar PUT, GET y DELETE por ID
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    lookup_field = 'id'

class IngresoListCreate(generics.ListCreateAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer
    
class IngresoDetail(generics.RetrieveUpdateDestroyAPIView):  # Vista para manejar PUT, GET y DELETE por ID
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer
    lookup_field = 'id'

class DetalleIngresoListCreate(generics.ListCreateAPIView):
    queryset = DetalleIngreso.objects.all()
    serializer_class = DetalleIngresoSerializer

class DetalleIngresoDetail(generics.RetrieveUpdateDestroyAPIView):  # Vista para manejar PUT, GET y DELETE por ID
    queryset = DetalleIngreso.objects.all()
    serializer_class = DetalleIngresoSerializer
    lookup_field = 'id'

class DetalleVentaListCreate(generics.ListCreateAPIView):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    
class DetalleVentaDetail(generics.RetrieveUpdateDestroyAPIView):  # Vista para manejar PUT, GET y DELETE por ID
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer
    lookup_field = 'id'

