from django.urls import path
from .views import *

urlpatterns = [
    path('inicio/', inicio, name='inicio'),
    path('padre/', padre, name='padre'),
    path('boxeador/', boxeador, name='boxeador'),

    path('boxeadores/', boxeadores, name='boxeadores'),
    path('boxeadoresFormulario/', boxeadoresFormulario, name='boxeadoresFormulario'),
    path('listarBoxeadores/', listarBoxeadores, name='listarBoxeadores'),
    path('editarBoxeador/<id>', editarBoxeador, name='editarBoxeador'),
    path('eliminarBoxeador/<id>', eliminarBoxeador, name='eliminarBoxeador'),

    path('boxeadoresFormulario/', boxeadoresFormulario, name='boxeadoresFormulario'),
    path('listarBoxeadores/', listarBoxeadores, name='listarboxeadores'),
    path('editarBoxeador/<id>', editarBoxeador, name='editarBoxeador'),
    path('eliminarBoxeador/<id>', eliminarBoxeador, name='eliminarBoxeador'),
    path('BoxeadoresBuscar/', boxeadorBuscar, name='boxeadorBuscar'),
    path('buscar_boxeador/', buscar_boxeador, name='buscar_boxeador'),
]

