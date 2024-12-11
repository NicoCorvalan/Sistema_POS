from django.urls import path
from .views import home,ArticuloListCreate, VentaListCreate, IngresoListCreate, DetalleIngresoListCreate, DetalleVentaListCreate

urlpatterns = [
    path('', home, name='home'),  # Página de inicio
    path('articulos/', ArticuloListCreate.as_view(), name='articulo-list-create'),
    path('ventas/', VentaListCreate.as_view(), name='venta-list-create'),
    path('ingresos/', IngresoListCreate.as_view(), name='ingreso-list-create'),
    path('detalles-ingreso/', DetalleIngresoListCreate.as_view(), name='detalle-ingreso-list-create'),
    path('detalles-venta/', DetalleVentaListCreate.as_view(), name='detalle-venta-list-create'),
]
