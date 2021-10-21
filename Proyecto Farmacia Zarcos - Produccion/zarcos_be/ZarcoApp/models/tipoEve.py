from django.db  import models

class TipoEve(models.Model):
    id              = models.BigAutoField(primary_key=True)
    tipo_evento     = models.CharField('Tipo Evento', max_length=100, blank=False, null=False)
    
    class Meta:
        verbose_name        = 'Tipo Evento'
        verbose_name_plural = 'Tipo de Eventos'
        ordering            = ['tipo_evento'] # ordena alfabeticamente

    def __str__(self): # nos permite visualizar por el nombre
        return self.tipo_evento