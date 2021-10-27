from rest_framework import serializers
from rest_framework.serializers import BaseSerializer
from ZarcoApp.models.evento import Evento
from ZarcoApp.models.lugar import Lugar
from ZarcoApp.models.categoria import Categoria
from ZarcoApp.models.tipoEve import TipoEve
from ZarcoApp.serializers.serializersCategorias import CategoriaSerializer
from ZarcoApp.serializers.serializersTipoevento import TipoEventoSerializer
from ZarcoApp.serializers.serializersLugar import LugarSerializer


class EventoSerializer(serializers.ModelSerializer):

    # categoria = CategoriaSerializer()
    # tipoEvento_FK = TipoEventoSerializer()
    # lugar_FK = LugarSerializer()

    class Meta:
        model = Evento
        fields = ['id', 'nombre_evento', 'categoria_FK', 'tipoEvento_FK', 'fecha', 'hora', 'duracion', 'lugar_FK', 'precio',
                  'cupo_maximo']

        # depth = 1 # Me trae toda la data

    def create(self, validated_data):
        print("Esta es la data que llega en el metodo created", validated_data)
        eventoInstance = Evento.objects.create(**validated_data)
        return eventoInstance

    def to_representation(self, obj):  # de objeto a json

        evento = Evento.objects.get(id=obj.id)
        categoria_FK = Categoria.objects.get(id=obj.categoria_FK.id)
        tipoEvento_FK = TipoEve.objects.get(id=obj.tipoEvento_FK.id)
        lugar_FK = Lugar.objects.get(id=obj.lugar_FK.id)

        return {
            "id": evento.id,
            "nombre_evento": evento.nombre_evento,
            "categoria_FK": {
                "id": categoria_FK.id,
                "nombre_categoria": categoria_FK.nombre_categoria
            },
            "tipoEvento_FK": {
                "id": tipoEvento_FK.id,
                "tipo_evento": tipoEvento_FK.tipo_evento
            },
            "fecha": evento.fecha,
            "hora":  evento.hora,
            "duracion": evento.duracion,
            "lugar_FK": {
                "id": lugar_FK.id,
                "ciudad": lugar_FK.ciudad,
                "direccion": lugar_FK.direccion,
                # "nombre_lugar" : lugar_FK.nombre_lugar,
                # "complex" : lugar_FK.complemento
            },
            "precio": evento.precio,
            # "descripcionSimple" : evento.descripcion_simple,
            # "descripcionCompleta" : evento.descripcion_completa,
            # "imagen" : evento.imagen,
            # "thumbnail" : evento.thumbnail,
            "cupo_maximo": evento.cupo_maximo,
            # "is_active" : evento.is_active
        }
