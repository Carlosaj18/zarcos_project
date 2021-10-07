from django.db import models
from .categoria import Categoria
from .lugar import Lugar

class Evento(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombreEvento = models.CharField('NombreEvento', max_length = 100)
    tipo = models.CharField('Tipo', max_length = 20)
    categoriaFK = models.ForeignKey(Categoria, related_name='evento', max_length=10, on_delete=models.CASCADE) # 'categoria.Categoria'
    fecha = models.DateField() # The auto_now and auto_now_add options will always use the date in the default timezone at the moment of creation or update. If you need something different, you may want to consider using your own callable default or overriding save() instead of using auto_now or auto_now_add; or using a DateTimeField instead of a DateField and deciding how to handle the conversion from datetime to date at display time.
    hora = models.TimeField()
    duracion = models.IntegerField(default=0)
    lugarFK = models.ForeignKey(Lugar, related_name='evento', max_length=10, on_delete=models.CASCADE) # 'lugar.Lugar'
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    descripcionSimple = models.CharField('DescripcionSimple', max_length=256)
    descripcionCompleta = models.TextField()
    imagen = models.ImageField(height_field=None, width_field=None) # Requires the Pillow library && parametres (upload_to=None, height_field=None, width_field=None, max_length=100)
    thumbnail = models.ImageField(height_field=None, width_field=None)
    cupo_maximo = models.IntegerField(default=50) # It uses MinValueValidator and MaxValueValidator to validate the input based on the values that the default database supports.
    is_active = models.BooleanField(default=True)