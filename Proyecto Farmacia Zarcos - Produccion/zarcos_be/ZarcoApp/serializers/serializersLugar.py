from rest_framework import serializers
from ZarcoApp.models.lugar import Lugar

class LugarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lugar
        fields = ['id', 'ciudad', 'direccion', 'nombre_lugar', 'complemento']
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ['nombre_lugar'] # ordena alfabeticamente


    """ If we want to be able to return complete object instances based on the 
        validated data we need to implement one or both of the .create() and 
        .update() methods.  """

    def create(self, validated_data):
        return Lugar.objects.create(**validated_data)
    
    def to_representacion(self, obj):
            lugar = Lugar.objects.get(id=obj.id)
            return {
                "id" : lugar.id, 
                "ciudad" : lugar.nombre_categoria,
                "direccion" : lugar.direccion,
                "nombre_lugar" : lugar.nombre_lugar,
                "complemento" : lugar.complemento
            }
    