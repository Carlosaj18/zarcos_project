# Categoria
from .categoria.categoriaAPIView import CategoriaCreateAPIView, CategoriaAPIView, CategoriaDetailAPIView, CategoriaUpdateAPIView, CategoriaDeleteAPIView
from .categoria.categoriaViewSet import CategoriaViewSet
from .categoria.categoriaModelViewSet import CategoriaModelViewSet

# Evento
from .evento.eventoAPIView import EventoCreateAPIView, EventoAPIView, EventoDetailAPIView, EventoUpdateAPIView, EventoDeleteAPIView
from .evento.eventoViewSet import EventoViewSet
from .evento.eventoModelViewSet import EventoModelViewSet


# Inscripcion
from .inscripcion.inscripcionAPIView import InscripcionCreateAPIView, InscripcionAPIView, InscripcionDetailAPIView, InscripcionUpdateAPIView, InscripcionDeleteAPIView
from .inscripcion.inscripcionViewSet import InscripcionViewSet
from .inscripcion.inscripcionModelViewSet import InscripcionModelViewSet

# Lugar
from .lugar.lugarAPIView import LugarCreateAPIView, LugarAPIView, LugarDetailAPIView, LugarUpdateAPIView, LugarDeleteAPIView
from .lugar.lugarViewSet import LugarViewSet
from .lugar.lugarModelViewSet import LugarModelViewSet

# Persona
from .persona.personaAPIView import PersonaCreateAPIView, PersonaAPIView, PersonaDetailAPIView, PersonaUpdateAPIView, PersonaDeleteAPIView
from .persona.personaViewSet import PersonaViewSet
from .persona.personaModelViewSet import PersonaModelViewSet

# Tipo Evento
from .tipoEvento.tipoEventoAPIView import TipoEventoCreateAPIView, TipoEventoAPIView, TipoEventoDetailAPIView, TipoEventoUpdateAPIView, TipoEventoDeleteAPIView
from .tipoEvento.tipoEventoViewSet import TipoEventoViewSet
from .tipoEvento.tipoEventoModelViewSet import TipoEventoModelViewSet