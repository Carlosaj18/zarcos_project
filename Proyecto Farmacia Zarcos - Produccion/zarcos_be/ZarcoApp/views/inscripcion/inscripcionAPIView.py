from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from ZarcoApp.models.inscripcion import Inscripcion
from ZarcoApp.serializers.serializersInscripcion import InscripcionSerializer

""" Generics APIView"""

class InscripcionCreateAPIView(generics.CreateAPIView): 
    
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer # la data la vamos a hacer con la data del body para crear el objeto de la categoria
    # permission_class = [IsAuthenticated,]

    def post(self, request, *args, **kwargs): # metodo HTTP (POST, GET, PUSH, DELETE) 
                                    # recibe una data en el request del body 
                                    # *args argumentos basicos del servicio web 
                                    # **kwargs argumentos que se necesiten y que puedan llegar 
    
        print("request:", request)
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

        serializer = InscripcionSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class InscripcionAPIView(generics.ListAPIView):
    
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer
    # permission_classes = [IsAdminUser]

    def get(self, request):
        queryset = self.get_queryset()
        serializer = InscripcionSerializer(queryset, many=True)
        return Response(serializer.data)

class InscripcionDetailAPIView(generics.RetrieveAPIView):
    queryset = Inscripcion.objects.all()
    serializer_class = InscripcionSerializer 
    #permission_class = [IsAuthenticated,]
    
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

class InscripcionUpdateAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = InscripcionSerializer
    # permission_classes = [IsAdminUser]
    queryset = Inscripcion.objects.all()

    def put(self, request, *args, **kwargs):
        
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
    
class InscripcionDeleteAPIView(generics.RetrieveDestroyAPIView):
    serializer_class = InscripcionSerializer # la data la vamos a hacer con la data del body para crear el objeto de la categoria
    # permission_class = [IsAuthenticated,]
    queryset = Inscripcion.objects.all()

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

        return super().destroy(request, *args, **kwargs)
    
