from django.db import models


class Lugar(models.Model):
    id = models.BigAutoField(primary_key=True)
    ciudad = models.CharField('Ciudad', max_length=40)
    direccion = models.CharField('Direccion', max_length = 100)
    nombreLugar = models.CharField('Nombre_lugar', max_length = 100)
    complemento = models.CharField('Complemento', max_length = 256)
    
    REQUIRED_FIELDS={
        'Ciudad',
        'Direccion',
        'nombreLugar'
    }
    