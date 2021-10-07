from django.db import models

class Categoria(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombreCategoria = models.CharField('Categoria', max_length=100)