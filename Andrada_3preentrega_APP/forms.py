from django import forms


class Sectorform(forms.Form):
    nombre_sector=forms.CharField()
    numero_sector=forms.IntegerField()


class Empleadosform(forms.Form):   
    nombre=forms.CharField(max_length=30)
    apellido=forms.CharField(max_length=30)
    email=forms.EmailField()
    telefono=forms.IntegerField()

class Productoform(forms.Form):
    nombre=forms.CharField(max_length=200)
    categoria=forms.CharField(max_length=200)
    precio=forms.DecimalField(max_digits=10, decimal_places=2)
    