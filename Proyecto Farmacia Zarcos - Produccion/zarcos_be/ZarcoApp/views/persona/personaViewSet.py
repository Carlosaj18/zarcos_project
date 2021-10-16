from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404

from ZarcoApp.models.persona import User
from ZarcoApp.serializers.serializersPersona import PersonaSerializer

""" ViewSets"""

class PersonaViewSet(viewsets.ViewSet):

    def list(self, request):
            user = User.objects.all()
            serializer = PersonaSerializer(user, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = PersonaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PersonaSerializer(user)
        return Response(serializer.data)

    def update(self, request, pk=None):
        user = User.objects.get(pk=pk)
        serializer = PersonaSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None): # REVISAR
        user = User.objects.get(pk=pk)
        if user:
            user.state = False
            user.save()
            return Response({'message': 'User eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
