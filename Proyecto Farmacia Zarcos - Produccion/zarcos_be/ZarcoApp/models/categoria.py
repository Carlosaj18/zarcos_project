from django.db import models

class Categoria(models.Model):
    id               = models.BigAutoField(primary_key=True)
    nombre_categoria = models.CharField('Categoria', max_length=100, blank=False, null=False)

    def __str__(self): # nos permite visualizar por el nombre
        return self.nombre_categoria