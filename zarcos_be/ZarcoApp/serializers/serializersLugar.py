from rest_framework import serializers
from ZarcoApp.models.lugar import Lugar
from ZarcoApp.models.evento import Evento
from ZarcoApp.models.persona import Persona
from ZarcoApp.serializers.serializersEvento import EventoSerializer
from ZarcoApp.serializers.serializersPersona import PersonaSerializer

class LugarSerializer(serializers.ModelSerializer):

    persona = PersonaSerializer()
    evento = EventoSerializer()
    class Meta:
        model = Lugar
        fields = ['id', 'ciudad', 'direccion', 'nombreLugar', 'complemento', 'evento', 'persona']
    
    def create(self, validated_data):
        eventoData = validated_data.pop('evento')
        personaData = validated_data.pop('persona')
        lugarInstance = Lugar.objects.create(**validated_data)
        Persona.objects.create(lugarInstance=lugarInstance, **personaData)
        Evento.objects.create(lugarInstance=lugarInstance, **eventoData)
        return lugarInstance

    def to_representacion(self, obj): # de objeto a json
        lugar = Lugar.objects.get(id=obj.id)
        evento = Evento.objects.get(lugar=obj.id)
        persona = Persona.objects.get(lugar=obj.id)
        return {
            "id" : lugar.id,
                "ciudad"  : lugar.ciudad,
                "direccion" : lugar.direccion,
                "nombreLugar" : lugar.nombreLugar,
                "complemento" : lugar.complemento,
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
            }, 
            "persona" : {
                "id" : persona.id,
                "username" : persona.username,
                "email" : persona.email,
                "documento" : persona.documento,
                "nombres" : persona.nombres,
                "apellidos" : persona.apellidos,
                "telefono" : persona.telefono,
                "imagen"  : persona.imagen,
                "usuarioActivo" : persona.usuarioActivo,
                "usuarioAdministrador" : persona.usuarioAdministrador,
                "creacionUser" : persona.creacionUser,
                "password" : persona.password,

            }
        }
        
