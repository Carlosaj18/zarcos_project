from django.conf import settings
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from ZarcoApp.models.evento import Evento
from ZarcoApp.serializers.serializersEvento import EventoSerializer
        
class EventoCreateView(generics.CreateAPIView): # Para crear una categoria   
    
    serializer_class = EventoSerializer # la data la vamos a hacer con la data del body para crear el objeto de la categoria
    # permission_class = [IsAuthenticated,]

    class EventoCreateView(generics.CreateAPIView):
        
        def post(self, request, *args, **kwargs): # metodo HTTP (POST, GET, PUSH, DELETE)

            serializer = EventoSerializer(data=request.data['evento'])
            serializer.is_valid(raise_exception=True) # validacion de la data
            serializer.save() # llama al create del serializador para convertirlo en un objeto con los parametros del modelo categoria y que la data sea la misma y que la guarde en la base de datos

            return Response("Categoria creada con exito.", status=status.HTTP_201_CREATED)
