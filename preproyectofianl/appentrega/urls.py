from django.urls import path
from appentrega import views


urlpatterns = [
    path('', views.index),
    path('ver-personas/', views.ver_personas, name='ver_personas'),
    path('crear-persona/', views.inscribir_jugador, name='inscribir_jugador'),
    # path('admin/', admin.site.urls),
]