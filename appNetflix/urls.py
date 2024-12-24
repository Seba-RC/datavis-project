from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.Index, name='Index'),
    path('valoraciones', views.Valoraciones, name='Valoraciones'),
    path('usuarios', views.Usuarios, name='Valoraciones'),

    path('dataSerie',views.serie_data, name='datosSerie'),
    path('dataPelicula',views.pelicula_data, name='datosPelicula'),
    path('dataValoracionSerie',views.valoracionSerie_data, name='datosValoracionPelicula'),
    path('dataValoracionPelicula',views.valoracionPelicula_data, name='datosValoracionPelicula'),
    

    path('datatipoPelicula/<int:year>/', views.tipoPelicula_data, name='test'),
    path('datatipoSerie/<int:year>/', views.tipoSerie_data, name='test'),
    path('valoracionPromedioPeliculas/<int:year>/', views.valoracionPromedioPeliculas, name='test'),
    path('valoracionPromedioSeries/<int:year>/', views.valoracionPromedioSeries, name='test'),
    path('dataUsuario', views.dataUsuario, name='userData'),
]
