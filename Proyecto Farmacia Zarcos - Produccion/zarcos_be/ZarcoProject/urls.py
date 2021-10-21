"""ZarcoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from ZarcoApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    # CATEGORIA 
    path('categoria/', views.CategoriaCreateAPIView.as_view()),
    path('categoriaLista/', views.CategoriaAPIView.as_view()),
    path('categoria/<int:pk>/', views.CategoriaDetailAPIView.as_view()),
    path('categoria/update/<int:pk>/', views.CategoriaUpdateAPIView.as_view()),
    path('categoria/remove/<int:pk>/', views.CategoriaDeleteAPIView.as_view()),

    # EVENTO 
    path('evento/', views.EventoCreateAPIView.as_view()),
    path('eventoLista/', views.EventoAPIView.as_view()),
    path('evento/<int:pk>/', views.EventoDetailAPIView.as_view()),
    path('evento/update/<int:pk>/', views.EventoUpdateAPIView.as_view()),
    path('evento/remove/<int:pk>/', views.EventoDeleteAPIView.as_view()),

    # INSCRIPCION
    path('inscripcion/', views.InscripcionCreateAPIView.as_view()),
    path('inscripcionLista/', views.InscripcionAPIView.as_view()),
    path('inscripcion/<int:pk>/', views.InscripcionDetailAPIView.as_view()),
    path('inscripcion/update/<int:pk>/', views.InscripcionUpdateAPIView.as_view()),
    path('inscripcion/remove/<int:pk>/', views.InscripcionDeleteAPIView.as_view()),

    # LUGAR
    path('lugar/', views.LugarCreateAPIView.as_view()),
    path('lugarLista/', views.LugarAPIView.as_view()),
    path('lugar/<int:pk>/', views.LugarDetailAPIView.as_view()),
    path('lugar/update/<int:pk>/', views.LugarUpdateAPIView.as_view()),
    path('lugar/remove/<int:pk>/', views.LugarDeleteAPIView.as_view()),

    # PERSONA 
    path('persona/', views.PersonaCreateAPIView.as_view()),
    path('personaLista/', views.PersonaAPIView.as_view()),
    path('persona/<int:pk>/', views.PersonaDetailAPIView.as_view()),
    path('persona/update/<int:pk>/', views.PersonaUpdateAPIView.as_view()),
    path('persona/remove/<int:pk>/', views.PersonaDeleteAPIView.as_view()),

    # TIPO EVENTO
    path('tipoEvento/', views.TipoEventoCreateAPIView.as_view()),
    path('tipoEventoLista/', views.TipoEventoAPIView.as_view()),
    path('tipoEvento/<int:pk>/', views.TipoEventoDetailAPIView.as_view()),
    path('tipoEvento/update/<int:pk>/', views.TipoEventoUpdateAPIView.as_view()), 
    path('tipoEvento/remove/<int:pk>/', views.TipoEventoDeleteAPIView.as_view()),
]

