"""
Una vez los modelos han sido exportados en el módulo, se 
pueden registrar en la aplicación.

"""

from django.contrib import admin
from .models.categoria import Categoria
from .models.evento import Evento
from .models.inscripcion import Inscripcion
from .models.lugar import Lugar
from .models.persona import User
from .models.tipoEve import TipoEve

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Evento)
admin.site.register(Inscripcion)
admin.site.register(Lugar)
admin.site.register(User)
admin.site.register(TipoEve)