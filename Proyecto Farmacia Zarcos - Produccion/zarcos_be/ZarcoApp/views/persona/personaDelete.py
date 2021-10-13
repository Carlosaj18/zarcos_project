from django.conf import settings
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ZarcoApp.models.persona import User
from ZarcoApp.serializers.serializersPersona import PersonaSerializer 
     
class PersonaDeleteView(generics.DestroyAPIView):
    serializer_class = PersonaSerializer # la data la vamos a hacer con la data del body para crear el objeto de la categoria
    permission_class = [IsAuthenticated,]
    queryset = User.objects.all()


    def get(self, request, *args, **kwargs):
        print("Request:", request)
        print("Args", args)
        print("Kwargs", kwargs)
    
        """Validation tocken"""

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        # print("Antes de la validacion")
        if valid_data['user_id'] != kwargs['pk']: 
            # print("Despues de la validacion") 
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
             
        return super().destroy(request, *args, **kwargs)

        # JWT 
        # Revisar el tema del tocken 
        # Revisar el tema de get. tocken