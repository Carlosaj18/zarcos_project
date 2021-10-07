from rest_framework import serializers
from ZarcoApp.models.evento import Evento
from ZarcoApp.models.inscripcion import Inscripcion
from ZarcoApp.serializers.serializersInscripcion import InscripcionSerializer

class EventoSerializer(serializers.ModelSerializer):

    InscripcionSerializer()
    class Meta:
        model = Evento
        fields = ['id', 'nombreEvento', 'tipo', 'fecha', 'hora', 'duracion', 'precio', 'descripcionSimple', 
                'descripcionCompleta', 'imagen', 'thumbnail', 'cupo_maximo', 'is_active', 'inscripcion']

    def create(self, validated_data):
        inscripcionData = validated_data.pop('inscripcion')
        eventoInstance = Evento.objects.create(**validated_data)
        Inscripcion.objects.create(eventoInstance=eventoInstance, **inscripcionData)
        return eventoInstance
    
    def to_representacion(self, obj): # de objeto a json
        evento = Evento.objects.get(id=obj.id)
        inscripcion = Inscripcion.objects.get(evento=obj.id)
        return {
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
            "inscripcion" : {
                "id" : inscripcion.id,
                "numeroEntradas" : inscripcion.numeroEntradas,
                "pagoTotal" : inscripcion.pagoTotal,
                "fechaRegistro" : inscripcion.fechaRegistro,
            }
        }
