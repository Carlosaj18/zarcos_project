from django.conf import settings
from rest_framework import generics, status 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ZarcoApp.models.tipoEve import TipoEve
from ZarcoApp.serializers.serializersTipoevento import TipoeventoSerializer
        

class TipoEventoView(generics.ListCreateAPIView):
    queryset = TipoEve.objects.all()
    serializer_class = TipoeventoSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TipoeventoSerializer(queryset, many=True)
        return Response(serializer.data)

class TipoEventoDetailView(generics.RetrieveAPIView):
    serializer_class = TipoeventoSerializer
    # permission_classes = [IsAdminUser]
    queryset = TipoEve.objects.all()

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

        return super().get(request, *args, **kwargs)