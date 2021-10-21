from rest_framework                           import serializers
from ZarcoApp.models.inscripcion              import Inscripcion
from ZarcoApp.models.evento                   import Evento
from ZarcoApp.models.persona                  import User
from ZarcoApp.serializers.serializersPersona  import PersonaSerializer
from ZarcoApp.serializers.serializersEvento   import EventoSerializer

class InscripcionSerializer(serializers.ModelSerializer):

    # persona_FK = PersonaSerializer()
    # evento_FK = EventoSerializer()
    class Meta:
        model = Inscripcion
        fields = ['id', 'persona_FK', 'evento_FK','numero_entradas', 'pago_total', 'fecha_registro']
    
    def create(self, validated_data):         
        inscripcionInstance = Inscripcion.objects.create(**validated_data)
        return inscripcionInstance

    def to_representation(self, obj): # de objeto a json
        
        inscripcion = Inscripcion.objects.get(id=obj.id)
        evento_FK = Evento.objects.get(id=obj.evento_FK.id)
        persona_FK = User.objects.get(id=obj.persona_FK.id)
            
        return {
                    "id" : inscripcion.id,
                    "persona_FK" : {
                        "id" : persona_FK.id,
                        "username" : persona_FK.username,
                        "email" : persona_FK.email,
                        "documento" : persona_FK.documento,
                        "nombres" : persona_FK.nombres,
                        "apellidos" : persona_FK.apellidos,
                        "telefono" : persona_FK.telefono,
                        "ciudad"   : persona_FK.ciudad,
                        "direccion" : persona_FK.direccion,
                        # "imagen"  : persona_FK.imagen,
                        "usuario_activo" : persona_FK.usuario_activo,
                        "usuario_administrador" : persona_FK.usuario_administrador,
                        "creacion_user" : persona_FK.creacion_user,
                        "password" : persona_FK.password,
                    },
                    "evento_FK" : {
                        "id" : evento_FK.id, 
                        "nombre_evento" : evento_FK.nombre_evento,
                        "fecha" : evento_FK.fecha,
                        "hora" : evento_FK.hora,
                        "duracion" : evento_FK.duracion,
                        "precio" : evento_FK.precio,
                        "descripcionSimple" : evento_FK.descripcion_simple,
                        "descripcionCompleta" : evento_FK.descripcion_completa,
                        # "imagen" : evento_FK.imagen,
                        # "thumbnail" : evento_FK.thumbnail,
                        "cupo_maximo" : evento_FK.cupo_maximo,
                        "is_active" : evento_FK.is_active,
                    }, 
                    "numeroEntradas" : inscripcion.numero_entradas,
                    "pagoTotal" : inscripcion.pago_total,
                    "fechaRegistro" : inscripcion.fecha_registro,
                }

