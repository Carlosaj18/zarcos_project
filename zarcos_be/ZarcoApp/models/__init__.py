# https://docs.djangoproject.com/en/3.2/ref/models

"""
Ahora que se ha finalizado la implementación de los modelos, se debe realizar una serie de pasos que 
permitan integrarlos al módulo y a la aplicación. Primero se debe exportar los modelos en el módulo
models, para esto bastará con llamarlos en el archivo.

"""

from .categoria import Categoria
from .evento import Evento
from .inscripcion import Inscripcion
from .lugar import Lugar
from .persona import User