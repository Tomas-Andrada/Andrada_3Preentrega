from django.contrib import admin
from .models import Empleados, Sector, Producto

admin.site.register(Empleados)
admin.site.register(Sector)
admin.site.register(Producto)