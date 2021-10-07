from rest_framework import serializers
from ZarcoApp.models.persona import Persona
from ZarcoApp.models.inscripcion import Inscripcion
from ZarcoApp.serializers.serializersInscripcion import InscripcionSerializer

class PersonaSerializer(serializers.ModelSerializer):

    # Primer metodo para vincular otras tablas (se usa donde esta la FK) y se vincula todas
    inscripcion = InscripcionSerializer() # nos traemos el serializador de lugar

    class Meta:
        model = Persona
        fields = ['id', 'username', 'email', 'documento', 'nombres', 'apellidos', 'telefono', 'imagen', 'usuarioActivo', 'usuarioAdministrador', 'creacionUser', 'password', 'inscripcion']
        # exclude = ['id', 'username', 'email', 'documento'] se pueden excluir algunos campos

    def create(self,validated_data):
        inscripcionData = validated_data.pop('inscripcion')
        personaInstance = Persona.objects.create(**validated_data)
        Inscripcion.objects.create(persona=personaInstance, **inscripcionData)
        return personaInstance
    
    def to_representacion(self, obj):
        persona = Persona.objects.get(id=obj.id)
        inscripcion = Inscripcion.objects.get(persona=obj.id)
        return {
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
            "inscripcion" : {
                "id" : inscripcion.id,
                "numeroEntradas" : inscripcion.numeroEntradas,
                "pagoTotal" : inscripcion.pagoTotal,
                "fechaRegistro" : inscripcion.fechaRegistro,
            }
        }