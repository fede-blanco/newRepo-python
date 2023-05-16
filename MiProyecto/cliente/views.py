from django.shortcuts import render

# Debemos importar el modelo para poder utilizarlo
from .models import Cliente

# Create your views here.
def index(request):

  # instanciamos una variable con la lista de clientes
  clientes = Cliente.objects.all() #--> objects.all() trae todos los objetos de ese modelo en la base de datos

# creamos un contexto que le pasaremos a la vista para poder utilizar su contenido
  datos = { "clientes": clientes}

  # En este caso debemos agregar la carpeta que creamos dentro de templates porque django lo busca directamente dentro de templates
  return render(request, "cliente/index_cliente.html", datos)