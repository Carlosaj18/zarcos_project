from rest_framework import serializers

from ZarcoApp.models.evento import Evento
from ZarcoApp.models.lugar import Lugar
from ZarcoApp.models.categoria import Categoria
from ZarcoApp.models.tipoEve import TipoEve

class EventoSerializer(serializers.ModelSerializer):

    """categoria_FK = CategoriaSerializer()
    tipo_FK = TipoeventoSerializer()
    lugar_FK = LugarSerializer()
    inscripcion_FK = InscripcionSerializer()"""

    class Meta:
        model = Evento
        fields = ['id', 'nombre_evento', 'categoria_FK', 'tipoEvento_FK', 'fecha', 'hora', 'duracion', 'lugar_FK', 'precio', 'descripcion_simple', 
                'descripcion_completa', 'imagen', 'thumbnail', 'cupo_maximo', 'is_active']
        
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['nombre_evento', 'fecha'] # ordena alfabeticamente

    """def create(self, validated_data): -> REVISAR

        lugarData = validated_data.pop('lugar_FK')
        categoriaData = validated_data.pop('categoria_FK')
        tipoEventoData = validated_data.pop('tipoEvento_FK')
        eventoInstance = Evento.objects.create(**validated_data)
        Lugar.objects.create(eventoInstance=eventoInstance, **lugarData)
        Categoria.objects.create(eventoInstance=eventoInstance, **categoriaData)
        TipoEve.objects.create(eventoInstance=eventoInstance, **tipoEventoData)
        
        return eventoInstance"""
    
    def to_representacion(self, obj): # de objeto a json
        
        categoria_FK = Categoria.objects.get(id=obj.categoria_FK)
        tipoEvento_FK = TipoEve.objects.get(id=obj.tipoEvento_FK)
        lugar_FK = Lugar.objects.get(id=obj.lugar_FK)
        evento = Evento.objects.get(id=obj.id)
    
        return {
            "id" : evento.id, 
            "nombre_evento" : evento.nombreEvento,
            "categoria_FK" : {
                "id" : categoria_FK.id,
                "nombre_categoria" : categoria_FK.nombre_categoria
            },
            "tipoEvento_FK" : {
                "id" : tipoEvento_FK.id,
                "tipo_evento" : tipoEvento_FK.tipo_evento
            },
            "fecha" : evento.fecha,
            "hora" : evento.hora,
            "duracion" : evento.duracion,
            "lugar_FK" : {
                "id" : lugar_FK.id,
                "ciudad" : lugar_FK.ciudad,
                "direccion" : lugar_FK.direccion,
                "nombre_lugar" : lugar_FK.nombre_lugar,
                "complex" : lugar_FK.complemento
            },
            "precio" : evento.precio,
            "descripcionSimple" : evento.descripcionSimple,
            "descripcionCompleta" : evento.descripcionCompleta,
            "imagen" : evento.imagen,
            "thumbnail" : evento.thumbnail,
            "cupo_maximo" : evento.cupo_maximo,
            "is_active" : evento.is_active
        }
