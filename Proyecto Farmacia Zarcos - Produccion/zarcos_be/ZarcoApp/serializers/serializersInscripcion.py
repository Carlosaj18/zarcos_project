from rest_framework import serializers

from ZarcoApp.models.inscripcion import Inscripcion
from ZarcoApp.models.evento import Evento
from ZarcoApp.models.persona import User

class InscripcionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inscripcion
        fields = ['id', 'persona_FK', 'evento_FK','numero_entradas', 'pago_total', 'fecha_registro']
        verbose_name = 'Inscripcion'
        verbose_name_plural = 'Inscripciones'
        ordering = ['fecha_registro'] # ordena alfabeticamente

    """def create(self, validated_data): -> REVISAR
        personaData = validated_data.pop('persona')
        eventoData = validated_data.pop('evento')
        inscripcionInstance = Inscripcion.objects.create(**validated_data)
        User.objects.create(inscripcion=inscripcionInstance, **personaData)
        Evento.objects.create(inscripcion=inscripcionInstance, **eventoData)
        return inscripcionInstance"""

    def to_representacion(self, obj): # de objeto a json
        evento_FK = Evento.objects.get(id=obj.evento_FK)
        persona_FK = User.objects.get(id=obj.persona_FK)
        inscripcion = Inscripcion.objects.get(id=obj.id)

        return {
            "id" : inscripcion.id,
            "evento_FK" : {
                "id" : evento_FK.id, #
                "nombre_evento" : evento_FK.nombreEvento,
                "fecha" : evento_FK.fecha,
                "hora" : evento_FK.hora,
                "duracion" : evento_FK.duracion,
                "precio" : evento_FK.precio,
                "descripcionSimple" : evento_FK.descripcionSimple,
                "descripcionCompleta" : evento_FK.descripcionCompleta,
                "imagen" : evento_FK.imagen,
                "thumbnail" : evento_FK.thumbnail,
                "cupo_maximo" : evento_FK.cupo_maximo,
                "is_active" : evento_FK.is_active,
            }, 
            "persona" : {
                "id" : persona_FK.id,
                "username" : persona_FK.username,
                "email" : persona_FK.email,
                "documento" : persona_FK.documento,
                "nombres" : persona_FK.nombres,
                "apellidos" : persona_FK.apellidos,
                "telefono" : persona_FK.telefono,
                "imagen"  : persona_FK.imagen,
                "usuario_activo" : persona_FK.usuarioActivo,
                "usuario_administrador" : persona_FK.usuarioAdministrador,
                "creacion_user" : persona_FK.creacionUser,
                "password" : persona_FK.password,

            }, 
            "numeroEntradas" : inscripcion.numeroEntradas,
            "pagoTotal" : inscripcion.pagoTotal,
            "fechaRegistro" : inscripcion.fechaRegistro,
        }

