from .views.evento.eventoModelViewSet import EventoModelViewSet
from .views.evento.eventoViewSet import EventoViewSet
from .views.inscripcion.inscripcionViewSet import InscripcionViewSet
from .views.lugar.lugarViewSet import LugarViewSet
from .views.persona.personaViewSet import PersonaViewSet
from .views.tipoEvento.tipoEventoModelViewSet import TipoEventoModelViewSet
from .views.categoria.categoriaViewSet import CategoriaViewSet
from .views.categoria.categoriaModelViewSet import CategoriaModelViewSet
from .views.inscripcion.inscripcionModelViewSet import InscripcionModelViewSet
from .views.lugar.lugarModelViewSet import LugarModelViewSet
from .views.persona.personaModelViewSet import PersonaModelViewSet
from .views.tipoEvento.tipoEventoModelViewSet import TipoEventoModelViewSet
from .views.tipoEvento.tipoEventoViewSet import TipoEventoViewSet

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categoria', CategoriaViewSet,  basename='categoria')
router.register('categoria', CategoriaModelViewSet, basename='categoria1')
router.register('evento', EventoViewSet,  basename='evento')
router.register('evento', EventoModelViewSet, basename='evento')
router.register('inscripcion', InscripcionViewSet,  basename='inscripcion')
router.register('inscripcion', InscripcionModelViewSet, basename='inscripcion')
router.register('lugar', LugarViewSet,  basename='lugar')
router.register('lugar', LugarModelViewSet, basename='lugar')
router.register('user', PersonaViewSet,  basename='user')
router.register('user', PersonaModelViewSet, basename='user')
router.register('tipoEvento', TipoEventoViewSet,  basename='tipoEvento')
router.register('tipoEvento', TipoEventoModelViewSet, basename='tipoEvento')


urlpatterns = [
    # path('viewset/<int:pk>/', include(router.urls)),
    path('viewset/', include(router.urls)),
    path('modelviewset/', include(router.urls)),
]
