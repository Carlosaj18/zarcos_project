from rest_framework          import serializers
from ZarcoApp.models.persona import User

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'documento', 'nombres', 'apellidos', 'telefono', 'ciudad', 'direccion', 'imagen', 'usuario_activo', 'usuario_administrador', 
                'creacion_user', 'password']
        