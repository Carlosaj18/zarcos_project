from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404

from ZarcoApp.models.tipoEve import TipoEve
from ZarcoApp.serializers.serializersTipoevento import TipoeventoSerializer

""" ViewSets"""

class TipoEventoViewSet(viewsets.ViewSet):

    def list(self, request):
            tipoEvento = TipoEve.objects.all()
            serializer = TipoeventoSerializer(tipoEvento, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = TipoeventoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = TipoEve.objects.all()
        tipoEvento = get_object_or_404(queryset, pk=pk)
        serializer = TipoeventoSerializer(tipoEvento)
        return Response(serializer.data)

    def update(self, request, pk=None):
        tipoEvento = TipoEve.objects.get(pk=pk)
        serializer = TipoeventoSerializer(tipoEvento, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None): # REVISAR
        tipoEvento = TipoEve.objects.get(pk=pk)
        if tipoEvento:
            tipoEvento.state = False
            tipoEvento.save()
            return Response({'message': 'Tipo de Evento eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un tipo de evento con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
