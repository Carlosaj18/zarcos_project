from django.db import models


class Lugar(models.Model):
    id          = models.BigAutoField(primary_key=True)
    ciudad      = models.CharField('Ciudad', max_length=40, blank=False, null=False)
    direccion   = models.CharField('Direccion', max_length = 100, blank=False, null=False)
    nombre_lugar = models.CharField('Nombre_lugar', max_length = 100, blank=False, null=False)
    complemento = models.CharField('Complemento', max_length = 256)
    
    REQUIRED_FIELDS = {
        'Ciudad',
        'Direccion',
        'nombreLugar'
    }
    
    def __str__(self): # nos permite visualizar por el nombre
        return self.nombre_lugar