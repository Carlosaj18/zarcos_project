from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404


from ZarcoApp.models.inscripcion import Inscripcion
from ZarcoApp.serializers.serializersInscripcion import InscripcionSerializer

""" ViewSets"""

class InscripcionViewSet(viewsets.ViewSet):

    def list(self, request):
            inscripcion = Inscripcion.objects.all()
            serializer = InscripcionSerializer(inscripcion, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = InscripcionSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Inscripcion.objects.all()
        inscripcion = get_object_or_404(queryset, pk=pk)
        serializer = InscripcionSerializer(inscripcion)
        return Response(serializer.data)

    def update(self, request, pk=None):
        inscripcion = Inscripcion.objects.get(pk=pk)
        serializer = InscripcionSerializer(inscripcion, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None): # REVISAR
        inscripcion = Inscripcion.objects.get(pk=pk)
        if inscripcion:
            inscripcion.state = False
            inscripcion.save()
            return Response({'message': 'Inscripcion eliminada correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una inscripcion estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
