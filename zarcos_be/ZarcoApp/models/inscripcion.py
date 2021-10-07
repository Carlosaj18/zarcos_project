from django.db import models
from .persona import User
from .evento import Evento


class Inscripcion(models.Model):
    id = models.BigAutoField(primary_key=True)
    personaFK = models.ForeignKey(User, related_name='personaFK', max_length=10, on_delete=models.CASCADE)
    eventoFK = models.ForeignKey(Evento, related_name='eventoFK', max_length=10, on_delete=models.CASCADE) 
    numeroEntradas = models.IntegerField(default=1)
    pagoTotal = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    fechaRegistro = models.DateTimeField(auto_now_add=True)
    
    REQUIRED_FIELDS={
        'personaFK',
        'eventoFK',
        'numeroEntradas',
        'pagoTotal',
        'fechaRegistro'
    }