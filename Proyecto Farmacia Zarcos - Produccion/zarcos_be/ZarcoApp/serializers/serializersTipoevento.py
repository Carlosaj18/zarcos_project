from rest_framework                         import serializers
from ZarcoApp.models.tipoEve                import TipoEve

class TipoeventoSerializer(serializers.ModelSerializer):

    class Meta:
        model  = TipoEve
        fields = ['id', 'tipo_evento']
        verbose_name = 'Tipo Evento'
        verbose_name_plural = 'Tipo de Eventos'
        ordering = ['tipo_evento'] # ordena alfabeticamente

    
