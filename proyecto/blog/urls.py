from django.urls import path
from . import views #Importamos las vistas de la aplicación

urlpatterns=[
    path('',views.home, name='home'), #Definir la ruta principal de la aplicación blog
]