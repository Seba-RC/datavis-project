import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView 
from .models import *
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Avg
from django.db.models.functions import ExtractYear



# Create your views here.
def Index(request):
    return render(request, 'index.html')

def Valoraciones(request):
    return render(request, 'valoraciones.html')

def Usuarios(request):
    return render(request, 'usuarios.html')

def serie_data(request):
    data = list(Serie.objects.all().values())
    return JsonResponse(data, safe=False)
def pelicula_data(request):
    data = Pelicula.objects.all().values()
    return JsonResponse(list(data), safe=False)
def valoracionSerie_data(request):
    data = list(Valoracionserie.objects.all().values())
    return JsonResponse(data, safe=False)
def valoracionPelicula_data(request):
    data = list(Valoracionpelicula.objects.all().values())
    return JsonResponse(data, safe=False)
def usuario_data(request):
    data = list(Usuario.objects.all().values())
    return JsonResponse(data, safe=False)

# queries especificas:
# por tipo de pelicula
def tipoPelicula_data(request, year):
    tipoPelicula = (Pelicula.objects
                .values('tipopelicula')
                .exclude(tipopelicula='Documental')
                .annotate(
                    count=Count('tipopelicula'),
                    fechaTerminada=ExtractYear('fechaterminada')
                )
                .order_by('-count')).filter(fechaTerminada=year)
    result = list(tipoPelicula)
    return JsonResponse(result, safe=False)

def tipoSerie_data(request, year):
    tipoSerie = (Serie.objects
                .values('tiposerie')
                .exclude(tiposerie='Documental')
                .annotate(
                    count=Count('tiposerie'),
                    fechaTerminada=ExtractYear('fechaterminada')
                )
                .order_by('-count')).filter(fechaTerminada=year)
    result = list(tipoSerie)
    return JsonResponse(result, safe=False)

# Valoracion por genero de pelicula/serie
def valoracionPromedioPeliculas(request, year):
    valoracionPromedio = (
        Pelicula.objects
        .filter(valoracionpelicula__isnull=False) 
        .exclude(tipopelicula='Documental') 
        .values('tipopelicula')  
        .annotate(
            average_rating=Avg('valoracionpelicula__valoracionpelicula'), 
            fechaTerminada=ExtractYear('fechaterminada') 
        )
        .filter(fechaTerminada=year)
    )
    result = list(valoracionPromedio)
    return JsonResponse(result, safe=False)

def valoracionPromedioSeries(request, year):
    valoracionPromedio = (
        Serie.objects
        .filter(valoracionserie__isnull=False) 
        .exclude(tiposerie='Documental') 
        .values('tiposerie')  
        .annotate(
            average_rating=Avg('valoracionserie__valoracionserie'), 
            fechaTerminada=ExtractYear('fechaterminada') 
        )
        .filter(fechaTerminada=year)
    )
    result = list(valoracionPromedio)
    return JsonResponse(result, safe=False)



def dataUsuario(request):

    users = Usuario.objects.all()
    
    usuarioJoven = users.order_by('fechanacimiento').last()  
    usuarioViejo = users.order_by('fechanacimiento').first() 

    dataUsuarios = {
        'usuarios': list(users.values('idusuario', 'nombre', 'fechanacimiento', 'ciudad')),
        'usuarioJoven': {
            'idusuario': usuarioJoven.idusuario,
            'nombre': usuarioJoven.nombre,
            'fechanacimiento': usuarioJoven.fechanacimiento,
            'ciudad': usuarioJoven.ciudad,
        },
        'usuarioViejo': {
            'idusuario': usuarioViejo.idusuario,
            'nombre': usuarioViejo.nombre,
            'fechanacimiento': usuarioViejo.fechanacimiento,
            'ciudad': usuarioViejo.ciudad,
        }
    }

    return JsonResponse(dataUsuarios)
