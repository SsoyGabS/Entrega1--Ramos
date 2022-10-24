from django.urls import path
from appentrega import views


urlpatterns = [
    path('', views.index),
    path('ver-jugadores/', views.ver_jugadores, name='ver_jugadores'),
    path('inscribir-jugador/', views.inscribir_jugador, name='inscribir_jugador'),
    # path('admin/', admin.site.urls),
]