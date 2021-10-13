from django.conf import settings
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from ZarcoApp.models.evento import Evento
from ZarcoApp.serializers.serializersEvento import EventoSerializer
        

class EventoUpdateView(generics.UpdateAPIView):
    serializer_class = EventoSerializer
    # permission_classes = [IsAdminUser]
    queryset = Evento.objects.all()

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


