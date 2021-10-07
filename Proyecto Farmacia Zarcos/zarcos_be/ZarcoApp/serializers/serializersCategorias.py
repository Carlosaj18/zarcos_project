from rest_framework import serializers
from ZarcoApp.models.categoria import Categoria
from ZarcoApp.models.evento import Evento
from ZarcoApp.serializers.serializersEvento import EventoSerializer

class CategoriaSerializer(serializers.ModelSerializer):

    evento = EventoSerializer()
    class Meta:
        model = Categoria
        fields = ['id', 'nombreCategoria', 'evento']
    
    def create(self,validated_data): # de json a objeto
        eventoData = validated_data.pop('evento')
        categoriaInstance = Categoria.objects.create(**validated_data)
        Evento.objects.create(categoriaInstance=categoriaInstance, **eventoData)
        return categoriaInstance

    def to_representacion(self, obj): # de objeto a json
        categoria = Categoria.objects.get(id=obj.id)
        evento = Evento.objects.get(categoria=obj.id)
        return { # esto es lo que voy a retornar en el servicio web
            
            "id" : categoria.id, #
            "nombreCategoria" : categoria.nombreCategoria,
            "evento" : {
                "id" : evento.id, #
                "nombreEvento" : evento.nombreEvento,
                "tipo" : evento.tipo,
                "fecha" : evento.fecha,
                "hora" : evento.hora,
                "duracion" : evento.duracion,
                "precio" : evento.precio,
                "descripcionSimple" : evento.descripcionSimple,
                "descripcionCompleta" : evento.descripcionCompleta,
                "imagen" : evento.imagen,
                "thumbnail" : evento.thumbnail,
                "cupo_maximo" : evento.cupo_maximo,
                "is_active" : evento.is_active,
            }
        }

    
