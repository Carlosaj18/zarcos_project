from rest_framework import serializers
from ZarcoApp.models.persona import User

class PersonaSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'documento', 'nombres', 'apellidos', 'telefono', 'ciudad', 'direccion', 'imagen', 'usuario_activo', 'usuario_administrador', 
                'creacion_user', 'password']
        
    def create(self, validated_data):
            return User.objects.create(**validated_data)
    
    def to_representacion(self, obj):
        persona = User.objects.get(id=obj.id)
        return {
            "id" : persona.id,
            "username" : persona.username,
            "email" : persona.email,
            "documento" : persona.documento,
            "nombres" : persona.nombres,
            "apellidos" : persona.apellidos,
            "telefono" : persona.telefono,
            "ciudad" : persona.ciudad,
            "direccion" : persona.direccion,
            "imagen"  : persona.imagen,
            "usuario_activo" : persona.usuarioActivo,
            "usuario_administrador" : persona.usuarioAdministrador,
            "creacion_user" : persona.creacionUser,
            "password" : persona.password,

        }
