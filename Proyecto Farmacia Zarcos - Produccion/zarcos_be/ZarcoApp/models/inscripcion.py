from django.db  import models
from .persona   import User
from .evento    import Evento


class Inscripcion(models.Model):
    id               = models.BigAutoField(primary_key=True)
    persona_FK       = models.ForeignKey(User, related_name='inscripcion', max_length=10, on_delete=models.CASCADE)
    evento_FK        = models.ForeignKey(Evento, related_name='inscripcion', max_length=10, on_delete=models.CASCADE) 
    numero_entradas  = models.IntegerField(default=1, blank=False, null=False)
    pago_total       = models.DecimalField(max_digits=9, decimal_places=2, default=0.0)
    fecha_registro   = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'
        ordering = ['fecha_registro'] # ordena alfabeticamente
    
    REQUIRED_FIELDS = {
        'persona_FK',
        'evento_FK'
    }
    