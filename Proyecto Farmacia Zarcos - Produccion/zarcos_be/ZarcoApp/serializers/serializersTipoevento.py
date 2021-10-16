from rest_framework                         import serializers
from ZarcoApp.models.tipoEve                import TipoEve

class TipoeventoSerializer(serializers.ModelSerializer):

    class Meta:
        model  = TipoEve
        fields = ['id', 'tipo_evento']

    """ If we want to be able to return complete object instances based on the 
        validated data we need to implement one or both of the .create() and 
        .update() methods.  """

    def create(self, validated_data):
        return TipoEve.objects.create(**validated_data)
    
    def to_representacion(self, obj):
            tipoEvento = TipoEve.objects.get(id=obj.id)
            return {
                "id" : tipoEvento.id, 
                "tipo_evento" : tipoEvento.tipo_evento
            }