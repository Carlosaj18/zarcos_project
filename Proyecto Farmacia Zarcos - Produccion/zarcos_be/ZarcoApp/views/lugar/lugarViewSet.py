from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404


from ZarcoApp.models.lugar import Lugar
from ZarcoApp.serializers.serializersLugar import LugarSerializer

""" ViewSets"""

class LugarViewSet(viewsets.ViewSet):

    def list(self, request):
            inscripcion = Lugar.objects.all()
            serializer = LugarSerializer(inscripcion, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = LugarSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Lugar.objects.all()
        lugar = get_object_or_404(queryset, pk=pk)
        serializer = LugarSerializer(lugar)
        return Response(serializer.data)

    def update(self, request, pk=None):
        lugar = Lugar.objects.get(pk=pk)
        serializer = LugarSerializer(lugar, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None): # REVISAR
        lugar = Lugar.objects.get(pk=pk)
        if lugar:
            lugar.state = False
            lugar.save()
            return Response({'message': 'Lugar eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un lugar estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
