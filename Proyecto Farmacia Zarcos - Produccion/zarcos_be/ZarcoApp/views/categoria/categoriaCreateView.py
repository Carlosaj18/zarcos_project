from django.conf import settings
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from ZarcoApp.models.categoria import Categoria
from ZarcoApp.serializers.serializersCategorias import CategoriaSerializer
        
class CategoriaCreateView(generics.CreateAPIView): # Para crear una categoria   
    
    serializer_class = CategoriaSerializer # la data la vamos a hacer con la data del body para crear el objeto de la categoria
    # permission_class = [IsAuthenticated,]

    class CategoriaCreateView(generics.CreateAPIView):
        
        def post(self, request, *args, **kwargs): # metodo HTTP (POST, GET, PUSH, DELETE) 
                                        # recibe una data en el request del body 
                                        # *args argumentos basicos del servicio web 
                                        # **kwargs argumentos que se necesiten y que puedan llegar 
        
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

            serializer = CategoriaSerializer(data=request.data['categoria'])
            serializer.is_valid(raise_exception=True) # validacion de la data
            serializer.save() # llama al create del serializador para convertirlo en un objeto con los parametros del modelo categoria y que la data sea la misma y que la guarde en la base de datos
       
            return Response("Categoria creada con exito.", status=status.HTTP_201_CREATED)
