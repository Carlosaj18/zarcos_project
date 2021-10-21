from django.db   import models
from .categoria  import Categoria
from .lugar      import Lugar
from .tipoEve    import TipoEve

class Evento(models.Model):
    id                   = models.BigAutoField(primary_key=True)
    nombre_evento        = models.CharField('NombreEvento', max_length = 100, blank=False, null=False)
    categoria_FK         = models.ForeignKey(Categoria, related_name='evento_categoria', max_length=10, on_delete=models.CASCADE) # 'categoria.Categoria'
    tipoEvento_FK        = models.ForeignKey(TipoEve, related_name='evento_tipo', max_length=10, on_delete=models.CASCADE) # tipoEvento.TipoEvento
    fecha                = models.DateField(blank=False, null=False) # The auto_now and auto_now_add options will always use the date in the default timezone at the moment of creation or update. If you need something different, you may want to consider using your own callable default or overriding save() instead of using auto_now or auto_now_add; or using a DateTimeField instead of a DateField and deciding how to handle the conversion from datetime to date at display time.
    hora                 = models.TimeField(blank=False, null=False)
    duracion             = models.IntegerField(default=0, blank=False, null=False)
    lugar_FK             = models.ForeignKey(Lugar, related_name='evento_lugar', max_length=10, on_delete=models.CASCADE) # 'lugar.Lugar'
    precio               = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    descripcion_simple   = models.CharField('DescripcionSimple', max_length=256)
    descripcion_completa = models.TextField()
    imagen               = models.ImageField(height_field=None, width_field=None, blank=True, null=True) # Requires the Pillow library && parametres (upload_to=None, height_field=None, width_field=None, max_length=100)
    thumbnail            = models.ImageField(height_field=None, width_field=None, blank=True, null=True)
    cupo_maximo          = models.IntegerField(default=50) # It uses MinValueValidator and MaxValueValidator to validate the input based on the values that the default database supports.
    is_active            = models.BooleanField(default=True)
    
    class Meta: 
        verbose_name        = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering            = ['nombre_evento', 'fecha'] # ordena alfabeticamente
    

    def __str__(self): # nos permite visualizar por el nombre
        return self.nombre_evento