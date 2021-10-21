from rest_framework                         import serializers
from ZarcoApp.models.tipoEve                import TipoEve

class TipoEventoSerializer(serializers.ModelSerializer):

    class Meta:
        model  = TipoEve
        fields = ['id', 'tipo_evento']
