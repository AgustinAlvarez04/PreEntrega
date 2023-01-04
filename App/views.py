from django.shortcuts import render
from .models import Persona, Pais, Boxeador
from django.http import HttpResponse

from .forms import PersonaForm, PaisForm, BoxeadorForm

# Create your views here.
def inicio(request):
    return render (request, 'App/inicio.html')

def padre (request):
    return render (request, 'App/padre.html')

def boxeador (request):
    return render (request, 'App/boxeador.html')

def boxeadores (request):
    return render (request, 'App/boxeadores.html')

def boxeadorFormulario (request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            apellido = informacion["apellido"]
            fechaNacimiento = informacion["fechaNacimiento"]
            nacionalidad = informacion["nacionalidad"]
            tamanio = informacion["tamanio"]
            peso = informacion["peso"]
            boxeador = Persona(nombre=nombre, apellido=apellido, fechaNacimiento=fechaNacimiento, nacionalidad=nacionalidad, tamanio=tamanio, peso=peso)
            boxeador.save()
            boxeadores = Persona.objects.all()
            return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores, "parrafo":"Boxeador registrado correctamente"})
        else:
            return render (request, 'App/boxeadoresFormulario.html',{"form":form, "mensaje":"Error al registrar boxeador"})
    else:
        formulario = PersonaForm()
        return render (request, 'App/boxeadoresFormulario.html',{"form":formulario})

def listarBoxeadores(request):
    boxeadores = Persona.objects.all()
    return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores})

def editarBoxeador(request, id):
    boxeador = Persona.objects.get(id=id)
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            boxeador.nombre = info["nombre"]
            boxeador.apellido = info["apellido"]
            boxeador.fechaNacimiento = info["fechaNacimiento"]
            boxeador.nacionalidad = info["nacionalidad"]
            boxeador.tamanio = info["tamanio"]
            boxeador.peso = info["peso"]
            boxeador.save()
            boxeadores = Persona.objects.all()
            return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores, "parrafo":"Boxeador editado correctamente"})
        pass
    else:
        form= PersonaForm(initial={"nombre":boxeador.nombre, "apellido":boxeador.apellido, "fechaNacimiento":boxeador.fechaNacimiento, "nacionalidad":boxeador.nacionalidad, "tamanio":boxeador.tamanio, "peso":boxeador.peso})
        return render (request, 'App/editarBoxeador.html',{"form":form, "boxeador":boxeador})

def eliminarBoxeador(request, id):
    boxeador = Persona.objects.get(id=id)
    boxeador.delete()
    boxeadores = Persona.objects.all()
    return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores, "parrafo":"Boxeador eliminado correctamente"})


def boxeadoresFormulario (request):
    if request.method == 'POST':
        form = Box(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            nombre = informacion["nombre"]
            pais = informacion["pais"]
            fechaInicio = informacion["fechaInicio"]
            peso = informacion["peso"]
            categoria = Boxeador(nombre=nombre, pais=pais, fechaInicio=fechaInicio, peso=peso)
            boxeadores.save()
            boxeadores = Boxeador.objects.all()
            return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores, "parrafo":"boxeadores registrados correctamente"})
        else:
            return render (request, 'App/boxeadoresFormulario.html',{"form":form, "mensaje":"Error al registrar boxeador"})
    else:
        formulario = BoxeadorForm()
        return render (request, 'App/boxeadoresFormulario.html',{"form":formulario})

def listarBoxeadores(request):
    boxeadores = Boxeador.objects.all()
    return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores})

def editarBoxeadores(request, id):
    boxeador = Boxeador.objects.get(id=id)
    if request.method == 'POST':
        form = BoxeadorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            boxeador.nombre = info["nombre"]
            boxeador.pais = info["pais"]
            boxeador.apodo = info["apodo"]
            boxeador.categoria = info["categoria"]
            boxeador.save()
            boxeadores = Boxeador.objects.all()
            return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores, "parrafo":"Boxeador editado correctamente"})
        pass
    else:
        form= BoxeadorForm(initial={"pais":boxeador.pais, "nombre":boxeador.nombre, "apodo":boxeador.apodo, "colores":boxeador.colores, "fundacion":boxeador.fundacion, "web":boxeador.web, "diminutivo":boxeador.diminutivo})
        return render (request, 'App/editarBoxeador.html',{"form":form, "boxeador":boxeador})

def eliminarBoxeador(request, id):
    boxeador = Boxeador.objects.get(id=id)
    boxeador.delete()
    boxeadores = Boxeador.objects.all()
    return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores, "parrafo":"Boxeadores eliminado correctamente"})

def boxeadorBuscar(request):
    return render (request, 'App/boxeadorBuscar.html')

def buscar_boxeador(request):
    nombre=request.GET["nombre"]
    if nombre != "":
        boxeador = Boxeador.objects.filter(nombre__contains=nombre)
        return render (request, 'App/boxeadoresLista.html',{"boxeadores":boxeadores, "parrafo":"Resultado de la busqueda"})
    else:
        return render (request, 'App/boxeadorBuscar.html',{"mensaje":"Debe ingresar un nombre"})

