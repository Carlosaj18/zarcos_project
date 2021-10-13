from rest_framework import serializers
from ZarcoApp.models.persona import User
from ZarcoApp.models.lugar import Lugar

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'documento', 'nombres', 'apellidos', 'telefono', 'imagen', 'usuario_activo', 'usuario_administrador', 
                'creacion_user', 'password', 'lugar_FK']
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['username'] # ordena alfabeticamente

    """def create(self,validated_data): -> REVISAR
        lugarData = validated_data.pop('lugar')
        personaInstance = User.objects.create(**validated_data)
        Lugar.objects.create(persona=personaInstance, **lugarData)
        return personaInstance"""
    
    def to_representacion(self, obj):
        persona = User.objects.get(id=obj.id)
        lugar_FK = Lugar.objects.get(id=obj.lugar_FK)
        return {
            "id" : persona.id,
            "username" : persona.username,
            "email" : persona.email,
            "documento" : persona.documento,
            "nombres" : persona.nombres,
            "apellidos" : persona.apellidos,
            "telefono" : persona.telefono,
            "imagen"  : persona.imagen,
            "usuario_activo" : persona.usuarioActivo,
            "usuario_administrador" : persona.usuarioAdministrador,
            "creacion_user" : persona.creacionUser,
            "password" : persona.password,
            "lugar_FK" : {
                "id" : lugar_FK.id,
                "ciudad" : lugar_FK.ciudad,
                "direccion" : lugar_FK.direccion,
                "nombre_lugar" : lugar_FK.nombre_lugar,
                "complex" : lugar_FK.complemento
            }
        }