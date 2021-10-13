from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from ZarcoApp import views

urlpatterns = [
 path('admin/', admin.site.urls),
 path('login/', TokenObtainPairView.as_view()),
 path('refresh/', TokenRefreshView.as_view()),

 # POST 
 path('categoria/', views.CategoriaCreateView.as_view()),
 path('evento/', views.EventoCreateView.as_view()),
 path('inscripcion/', views.InscripcionCreateView.as_view()),
 path('lugar/', views.LugarCreateView.as_view()),
 path('persona/', views.PersonaCreateView.as_view()),
 path('tipoEvento/', views.TipoEventoCreateView.as_view()),

 # GET 
 path('categoriaLista/', views.CategoriaView.as_view()),
 path('categoria/<int:pk>', views.CategoriaDetailView.as_view()),
 path('eventoLista/', views.EventoView.as_view()),
 path('evento/<int:pk>', views.EventoDetailView.as_view()),
 path('inscripcionLista/', views.InscripcionView.as_view()),
 path('inscripcion/<int:pk>', views.InscripcionDetailView.as_view()),
 path('lugarLista/', views.LugarView.as_view()),
 path('lugar/<int:pk>', views.LugarDetailView.as_view()),
 path('tipoEventoLista/', views.TipoEventoView.as_view()),
 path('tipoEvento/<int:pk>', views.TipoEventoDetailView.as_view()),
 path('personaLista/', views.PersonaView.as_view()),
 path('persona/<int:pk>', views.PersonaDetailView.as_view()),

 
 # UPDATE
 path('categoria/update/<int:pk>', views.CategoriaUpdateView.as_view()),
 path('evento/update/<int:pk>', views.EventoUpdateView.as_view()),
 path('inscripcion/update/<int:pk>', views.InscripcionUpdateView.as_view()),
 path('lugar/update/<int:pk>', views.LugarUpdateView.as_view()),
 path('tipoEvento/update/<int:pk>', views.TipoEventoUpdateView.as_view()),
 path('persona/update/<int:pk>', views.PersonaUpdateView.as_view()),


 # DELETE 
 path('categoria/remove/<int:pk>', views.CategoriaDeleteView.as_view()),
 path('evento/remove/<int:pk>', views.EventoDeleteView.as_view()),
 path('inscripcion/remove/<int:pk>', views.InscripcionDeleteView.as_view()),
 path('lugar/remove/<int:pk>', views.LugarDeleteView.as_view()),
 path('tipoEvento/remove/<int:pk>', views.TipoEventoDeleteView.as_view()),
 path('persona/remove/<int:pk>', views.PersonaDeleteView.as_view()),

 # GET -> FILTRADO
 # path('categoria/<int:evento>/<int:pk>', views.CategoriaView.as_view()),
 # path('user/<int:pk>/', views.UserDetailView.as_view()),
]