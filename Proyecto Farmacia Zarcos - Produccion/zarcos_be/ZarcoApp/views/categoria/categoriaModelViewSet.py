from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from ZarcoApp.models.categoria import Categoria
from ZarcoApp.serializers.serializersCategorias import CategoriaSerializer



""" Model ViewSets"""

class CategoriaModelViewSet(viewsets.ModelViewSet): 
    
    serializer_class = CategoriaSerializer

    def get_queryset(self, pk=None):
        if pk is not None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        categoria_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(categoria_serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Categoria creada correctamente!'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def update(self,request, pk=None):
        if self.get_queryset(pk):
            categoria_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if categoria_serializer.is_valid():
                categoria_serializer.save()
                return Response(categoria_serializer.data, status = status.HTTP_200_OK)
            return Response(categoria_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk=None):
        categoria = Categoria.objects.get(pk=pk)
        if categoria:
            categoria.state = False
            categoria.save()
            return Response({'message': 'Categoria eliminada correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una categoria con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        