from django.urls import path
from Andrada_3preentrega_APP import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path("empleados/",views.empleados, name="Empleados"),
    path("sector/",views.sector,name="Sector"),
    path("productos/",views.productos,name="Productos"),
    path("buscarsector/",views.buscarsector,name="buscarsector"),
    path("buscar/",views.buscar,name="buscar"),
]