from django.urls import path
from .views import home,ArticuloListCreate, ArticuloDetail, VentaListCreate, IngresoListCreate, DetalleIngresoListCreate, DetalleVentaListCreate,VentaDetail, IngresoDetail, DetalleIngresoDetail, DetalleVentaDetail

urlpatterns = [
    path('', home, name='home'),
    path('articulos/', ArticuloListCreate.as_view(), name='articulo-list-create'),
    path('articulos/<int:id>/', ArticuloDetail.as_view(), name='articulo-detail'),  # Ruta para el detalle
    path('ventas/', VentaListCreate.as_view(), name='venta-list-create'),
    path('ventas/<int:id>/', VentaDetail.as_view(), name='venta-detail'),  # Ruta para el detalle
    path('ingresos/', IngresoListCreate.as_view(), name='ingreso-list-create'),
    path('ingresos/<int:id>/', IngresoDetail.as_view(), name='ingreso-detail'),  # Ruta para el detalle
    path('detalles-ingreso/', DetalleIngresoListCreate.as_view(), name='detalle-ingreso-list-create'),
    path('detalles-ingreso/<int:id>/', DetalleIngresoDetail.as_view(), name='detalle-ingreso-detail'),  # Ruta para el detalle
    path('detalles-venta/', DetalleVentaListCreate.as_view(), name='detalle-venta-list-create'),
    path('detalles-venta/<int:id>/', DetalleVentaDetail.as_view(), name='detalle-venta-detail'),  # Ruta para el detalle
]