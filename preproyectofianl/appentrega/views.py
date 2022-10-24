from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
from appentrega.forms import JugadorFormulario, BusquedaJugadorFormulario
from appentrega.models import Jugador
# Create your views here.}

def index(request):
    return render(request, 'appentrega/index.html')
def inscribir_jugador(request):
    
    if request.method == 'POST':
        
        formulario = JugadorFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
        
            nombre = data['nombre']
            apellido = data['apellido']
            edad = data['edad']
            fecha_inscripsion = data['fecha_inscripsion']
            if not fecha_inscripsion:
                fecha_inscripsion = datetime.now()
            
            jugador = Jugador(nombre=nombre, apellido=apellido, edad=edad, fecha_inscripsion=fecha_inscripsion)
            jugador.save()
            
            return redirect('ver_jugadores')
    
    formulario = JugadorFormulario()
    
    return render(request, 'appentrega/inscribir_jugador.html', {'formulario': formulario})
def ver_jugadores(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        jugadores = Jugador.objects.filter(nombre__icontains=nombre)
    else:
        jugadores = Jugador.objects.all()
    
    formulario = BusquedaJugadorFormulario()
    
    return render(request, 'appentrega/ver_jugador.html', {'jugadores': jugadores, 'formulario': formulario})