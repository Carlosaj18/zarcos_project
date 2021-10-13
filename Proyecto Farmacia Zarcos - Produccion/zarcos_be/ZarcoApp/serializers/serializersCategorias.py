from rest_framework                         import serializers
from ZarcoApp.models.categoria              import Categoria

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Categoria
        fields = ['id', 'nombre_categoria']
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['nombre_categoria'] # ordena alfabeticamente

