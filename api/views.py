from rest_framework import generics
from .models import Articulo, Venta, Ingreso, DetalleIngreso, DetalleVenta
from .serializers import ArticuloSerializer, VentaSerializer, IngresoSerializer, DetalleIngresoSerializer, DetalleVentaSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bienvenido a la API del Sistema POS")

class ArticuloListCreate(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class VentaListCreate(generics.ListCreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

class IngresoListCreate(generics.ListCreateAPIView):
    queryset = Ingreso.objects.all()
    serializer_class = IngresoSerializer

class DetalleIngresoListCreate(generics.ListCreateAPIView):
    queryset = DetalleIngreso.objects.all()
    serializer_class = DetalleIngresoSerializer

class DetalleVentaListCreate(generics.ListCreateAPIView):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer

