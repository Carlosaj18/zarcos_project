from rest_framework                         import serializers
from ZarcoApp.models.categoria              import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Categoria
        fields = ['id', 'nombre_categoria']
        
    """ If we want to be able to return complete object instances based on the 
        validated data we need to implement one or both of the .create() and 
        .update() methods.  """

    def create(self, validated_data):
        return Categoria.objects.create(**validated_data)
    
    def to_representacion(self, obj):
            categoria = Categoria.objects.get(id=obj.id)
            return {
                "id" : categoria.id, 
                "nombre_categoria" : categoria.nombre_categoria,
            }