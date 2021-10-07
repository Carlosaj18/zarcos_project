from rest_framework import serializers
from ZarcoApp.models.inscripcion import Inscripcion

class InscripcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscripcion
        fields = ['id', 'numeroEntradas', 'pagoTotal', 'fechaRegistro']

"""
    def create(self, validated_data):
        personaData = validated_data.pop('persona')
        eventoData = validated_data.pop('evento')
        inscripcionInstance = Inscripcion.objects.create(**validated_data)
        Persona.objects.create(inscripcion=inscripcionInstance, **personaData)
        Evento.objects.create(inscripcion=inscripcionInstance, **eventoData)
        return inscripcionInstance

    def to_representacion(self, obj): # de objeto a json
        inscripcion = Inscripcion.objects.get(id=obj.id)
        evento = Evento.objects.get(inscripcion=obj.id)
        persona = Persona.objects.get(inscripcion=obj.id)
        return {
            "id" : inscripcion.id,
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

            }, 
            "numeroEntradas" : inscripcion.numeroEntradas,
            "pagoTotal" : inscripcion.pagoTotal,
            "fechaRegistro" : inscripcion.fechaRegistro,
        }
"""  
