from django.conf import settings
from rest_framework import generics, status 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from ZarcoApp.models.persona import User
from ZarcoApp.serializers.serializersPersona import PersonaSerializer
        

class PersonaView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = PersonaSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = PersonaSerializer(queryset, many=True)
        return Response(serializer.data)

class PersonaDetailView(generics.RetrieveAPIView):
    serializer_class = PersonaSerializer
    # permission_classes = [IsAdminUser]
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):

        print("Request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        """Validation tocken = REVISAR LOS PERMISOS DE USUARIO

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
                 
        """

        return super().get(request, *args, **kwargs)