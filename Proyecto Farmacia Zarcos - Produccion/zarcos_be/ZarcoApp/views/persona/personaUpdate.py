from django.conf import settings
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ZarcoApp.models.persona import User
from ZarcoApp.serializers.serializersPersona import PersonaSerializer   

class PersonaUpdateView(generics.UpdateAPIView):
    serializer_class = PersonaSerializer
    # permission_classes = [IsAdminUser]
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        
        print("Request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        """Validation tocken

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
                
        """

        return super().update(request, *args, **kwargs)


