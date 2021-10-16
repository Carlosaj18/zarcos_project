from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from ZarcoApp import views


urlpatterns = [
 path('admin/', admin.site.urls),
 path('login/', TokenObtainPairView.as_view()),
 path('refresh/', TokenRefreshView.as_view()),

 # CATEGORIA 
 path('categoriaAPIView/', views.CategoriaCreateAPIView.as_view()),
 path('categoriaAPIViewLista/', views.CategoriaAPIView.as_view()),
 path('categoriaAPIView/<int:pk>/', views.CategoriaDetailAPIView.as_view()),
 path('categoriaAPIView/update/<int:pk>/', views.CategoriaUpdateAPIView.as_view()),
 path('categoriaAPIView/remove/<int:pk>/', views.CategoriaDeleteAPIView.as_view()),

 # EVENTO 
 path('eventoAPIView/', views.EventoCreateAPIView.as_view()),
 path('eventoAPIViewLista/', views.EventoAPIView.as_view()),
 path('eventoAPIView/<int:pk>/', views.EventoDetailAPIView.as_view()),
 path('eventoAPIView/update/<int:pk>/', views.EventoUpdateAPIView.as_view()),
 path('eventoAPIView/remove/<int:pk>/', views.EventoDeleteAPIView.as_view()),

 # INSCRIPCION
 path('inscripcionAPIView/', views.InscripcionCreateAPIView.as_view()),
 path('inscripcionAPIViewLista/', views.InscripcionAPIView.as_view()),
 path('inscripcionAPIView/<int:pk>/', views.InscripcionDetailAPIView.as_view()),
 path('inscripcionAPIView/update/<int:pk>/', views.InscripcionUpdateAPIView.as_view()),
 path('inscripcionAPIView/remove/<int:pk>/', views.InscripcionDeleteAPIView.as_view()),

 # LUGAR
 path('lugarAPIView/', views.LugarCreateAPIView.as_view()),
 path('lugarAPIViewLista/', views.LugarAPIView.as_view()),
 path('lugarAPIView/<int:pk>/', views.LugarDetailAPIView.as_view()),
 path('lugarAPIView/update/<int:pk>/', views.LugarUpdateAPIView.as_view()),
 path('lugarAPIView/remove/<int:pk>/', views.LugarDeleteAPIView.as_view()),

 # PERSONA 
 path('personaAPIView/', views.PersonaCreateAPIView.as_view()),
 path('personaAPIViewLista/', views.PersonaAPIView.as_view()),
 path('personaAPIView/<int:pk>/', views.PersonaDetailAPIView.as_view()),
 path('personaAPIView/update/<int:pk>/', views.PersonaUpdateAPIView.as_view()),
 path('personaAPIView/remove/<int:pk>/', views.PersonaDeleteAPIView.as_view()),

 # TIPO EVENTO
 path('tipoEventoAPIView/', views.TipoEventoCreateAPIView.as_view()),
 path('tipoEventoAPIViewLista/', views.TipoEventoAPIView.as_view()),
 path('tipoEventoAPIView/<int:pk>/', views.TipoEventoDetailAPIView.as_view()),
 path('tipoEventoAPIView/update/<int:pk>/', views.TipoEventoUpdateAPIView.as_view()), 
 path('tipoEventoAPIView/remove/<int:pk>/', views.TipoEventoDeleteAPIView.as_view()),

 # ViewSets
 path('', include('ZarcoApp.urls')),

 # FILTRADOS 

 # path('categoria/<int:evento>/<int:pk>', views.CategoriaView.as_view()),
 # path('user/<int:pk>/', views.UserDetailView.as_view()),
]