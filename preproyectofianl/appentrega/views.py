from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template, loader
from django.shortcuts import render, redirect
import random
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
            # v1
            fecha_creacion = data['fecha_creacion']
            if not fecha_creacion:
                fecha_creacion = datetime.now()
            
            # v2
            # fecha_creacion = data['fecha_creacion'] or datetime.now()
            
            persona = Jugador(nombre=nombre, apellido=apellido, edad=edad, fecha_creacion=fecha_creacion)
            persona.save()
            
            return redirect('ver_jugadores')
    
    formulario = JugadorFormulario()
    
    return render(request, 'home/crear_persona.html', {'formulario': formulario})
def ver_jugadores(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        jugadores = Jugador.objects.filter(nombre__icontains=nombre)
    else:
        jugadores = Jugador.objects.all()
    
    formulario = BusquedaJugadorFormulario()
    
    return render(request, 'home/ver_jugadores.html', {'jugadores': jugadores, 'formulario': formulario})