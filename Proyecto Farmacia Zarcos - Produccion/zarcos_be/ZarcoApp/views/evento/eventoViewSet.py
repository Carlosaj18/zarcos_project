from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404


from ZarcoApp.models.evento import Evento
from ZarcoApp.serializers.serializersEvento import EventoSerializer

""" ViewSets"""

class EventoViewSet(viewsets.ViewSet):

    def list(self, request):
            evento = Evento.objects.all()
            serializer = EventoSerializer(evento, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = EventoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Evento.objects.all()
        evento = get_object_or_404(queryset, pk=pk)
        serializer = EventoSerializer(evento)
        return Response(serializer.data)

    def update(self, request, pk=None):
        evento = Evento.objects.get(pk=pk)
        serializer = EventoSerializer(evento, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None): # REVISAR
        evento = Evento.objects.get(pk=pk)
        if evento:
            evento.state = False
            evento.save()
            return Response({'message': 'Evento eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un evento con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
