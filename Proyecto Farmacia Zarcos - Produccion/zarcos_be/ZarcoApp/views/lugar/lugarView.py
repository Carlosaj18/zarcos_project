from django.conf import settings
from rest_framework import generics, status 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from ZarcoApp.models.lugar import Lugar
from ZarcoApp.serializers.serializersLugar import LugarSerializer
        

class LugarView(generics.ListCreateAPIView):
    queryset = Lugar.objects.all()
    serializer_class = LugarSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = LugarSerializer(queryset, many=True)
        return Response(serializer.data)

class LugarDetailView(generics.RetrieveAPIView):
    serializer_class = LugarSerializer
    # permission_classes = [IsAdminUser]
    queryset = Lugar.objects.all()

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