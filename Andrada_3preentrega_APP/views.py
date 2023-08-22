from django.shortcuts import render,HttpResponse
from .models import Empleados,Sector,Producto
from .forms import Empleadosform,Productoform,Sectorform

def inicio(request):
        return render(request, 'AppAndrada/inicio.html')

def empleados(request):
    empleados = Empleados.objects.all()  
    if request.method == 'POST':
        miFormulario = Empleadosform(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            empleado = Empleados(
                nombre=informacion['nombre'],
                Apellido=informacion['apellido'],
                correo=informacion['email'],
                telefono=informacion['telefono']
            )
            empleado.save()
            miFormulario = Empleadosform()
            return render(request, "AppAndrada/empleados.html", {"empleados": empleados, "miFormulario": miFormulario, "mensaje": "Empleado creado"})
        else:
            return render(request, "AppAndrada/empleados.html", {"empleados": empleados, "miFormulario": miFormulario, "mensaje": "Datos inválidos"})
    else:
        miFormulario = Empleadosform()

    return render(request, "AppAndrada/empleados.html", {"empleados": empleados, "miFormulario": miFormulario})
 
def sector(request):
    sectores = Sector.objects.all()  # Cambié el nombre de la variable a "sectores"
    
    if request.method == 'POST':
        miFormulario = Sectorform(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nuevo_sector = Sector(
                nombre_sector=informacion['nombre_sector'],
                numero_sector=informacion['numero_sector']
            )
            nuevo_sector.save()
            miFormulario = Sectorform()
            return render(request, 'AppAndrada/sector.html', {"sectores": sectores, "miFormulario": miFormulario, "mensaje": "Sector creado"})
        else:
            return render(request, 'AppAndrada/sector.html', {"sectores": sectores, "miFormulario": miFormulario, "mensaje": "Datos inválidos"})
    else:
        miFormulario = Sectorform()
    
    return render(request, 'AppAndrada/sector.html', {"sectores": sectores, "miFormulario": miFormulario})

def productos(request):
    productos = Producto.objects.all() 
    if request.method == 'POST':
        miFormulario = Productoform(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            producto = Producto(
                nombre=informacion['nombre'],
                categoria=informacion['categoria'],
                precio=informacion['precio']
            )
            producto.save()
            miFormulario=Productoform()
            return render(request, "AppAndrada/productos.html", { "productos": productos,"miFormulario": miFormulario,"mensaje":"Producto creado"})
        else:
            return render(request, "AppAndrada/productos.html", {"productos": productos,"mensaje":"Datos invalidos"})
    else:
        miFormulario = Productoform()  
    return render(request, "AppAndrada/productos.html", {"productos": productos, "miFormulario": miFormulario})


def buscarsector(request):
    return render(request, "AppAndrada/buscarsector.html")
def buscar(request):
    numero = request.GET.get("sector", "")
    if numero!="":
        sectores = Sector.objects.filter(numero_sector__icontains=numero)
        return render(request, "AppAndrada/resultados.html", {"sectores": sectores, "numero": numero})
    else:
        return render(request, "AppAndrada/buscarsector.html",{"mensaje":"No enviaste datos"})
