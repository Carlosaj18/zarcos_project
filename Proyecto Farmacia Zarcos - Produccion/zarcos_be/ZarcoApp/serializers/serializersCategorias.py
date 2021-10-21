from rest_framework                         import serializers
from ZarcoApp.models.categoria              import Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Categoria
        fields = ['id', 'nombre_categoria']
        