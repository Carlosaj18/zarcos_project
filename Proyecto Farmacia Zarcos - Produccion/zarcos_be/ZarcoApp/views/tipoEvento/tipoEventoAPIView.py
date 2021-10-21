from django.conf                                import settings
from rest_framework                             import generics, status
from rest_framework.response                    import Response
from rest_framework.permissions                 import DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.backends          import TokenBackend
from rest_framework_simplejwt.serializers       import TokenObtainPairSerializer
from ZarcoApp.models.tipoEve                    import TipoEve
from ZarcoApp.serializers.serializersTipoevento import TipoEventoSerializer

""" Generics APIView"""
class TipoEventoCreateAPIView(generics.CreateAPIView): 
    
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [IsAdminUser]
    queryset = TipoEve.objects.all()
    serializer_class = TipoEventoSerializer

    def post(self, request, *args, **kwargs): # metodo HTTP (POST, GET, PUSH, DELETE) 
                                    # recibe una data en el request del body 
                                    # *args argumentos basicos del servicio web 
                                    # **kwargs argumentos que se necesiten y que puedan llegar 
        print("request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        serializer = TipoEventoSerializer(data=request.data)

        """Validation tocken 

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        
        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class TipoEventoAPIView(generics.ListAPIView):
    
    queryset = TipoEve.objects.all()
    serializer_class = TipoEventoSerializer
    # permission_classes = (IsAuthenticated,)

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
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""

        queryset = self.get_queryset()
        serializer = TipoEventoSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class TipoEventoDetailAPIView(generics.RetrieveAPIView):

    queryset = TipoEve.objects.all()
    serializer_class = TipoEventoSerializer
    # permission_classes = (IsAuthenticated,)
    
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
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
                
        return super().get(request, *args, **kwargs)
class TipoEventoUpdateAPIView(generics.RetrieveUpdateAPIView):
    
    queryset = TipoEve.objects.all()
    serializer_class = TipoEventoSerializer
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [IsAdminUser]

    def put(self, request, *args, **kwargs):
        
        print("Request:", request)
        print("Args", args)
        print("Kwargs", kwargs)

        """Validation tocken && Validation if it is AdminUser 

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)

        if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
  
        return super().update(request, *args, **kwargs)
    
class TipoEventoDeleteAPIView(generics.RetrieveDestroyAPIView):
    
    queryset = TipoEve.objects.all()
    serializer_class = TipoEventoSerializer
    # permission_classes = (IsAuthenticated,)
    # permission_classes = [IsAdminUser]

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
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)"""
            
        return super().destroy(request, *args, **kwargs)