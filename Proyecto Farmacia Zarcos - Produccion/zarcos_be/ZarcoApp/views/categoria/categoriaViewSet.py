from django.conf import settings
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404


from ZarcoApp.models.categoria import Categoria
from ZarcoApp.serializers.serializersCategorias import CategoriaSerializer

""" ViewSets"""

class CategoriaViewSet(viewsets.ViewSet):

    def list(self, request):
            categorias = Categoria.objects.all()
            serializer = CategoriaSerializer(categorias, many=True)
            return Response(serializer.data)

    def create(self, request):
        serializer = CategoriaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Categoria.objects.all()
        categoria = get_object_or_404(queryset, pk=pk)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

    def update(self, request, pk=None):
        categoria = Categoria.objects.get(pk=pk)
        serializer = CategoriaSerializer(categoria, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None): # REVISAR
        categoria = Categoria.objects.get(pk=pk)
        if categoria:
            categoria.state = False
            categoria.save()
            return Response({'message': 'Producto eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una categoria con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
