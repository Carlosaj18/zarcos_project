from rest_framework        import serializers
from ZarcoApp.models.lugar import Lugar

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ['id', 'ciudad', 'direccion', 'nombre_lugar', 'complemento']
        verbose_name = 'Lugar'
        verbose_name_plural = 'Lugares'
        ordering = ['nombre_lugar'] # ordena alfabeticamente
