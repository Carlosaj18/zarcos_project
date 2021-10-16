from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from ZarcoApp.models.evento import Evento
from ZarcoApp.serializers.serializersEvento import EventoSerializer


""" Model ViewSets"""

class EventoModelViewSet(viewsets.ModelViewSet): 
    
    serializer_class = EventoSerializer

    def get_queryset(self, pk=None):
        if pk is not None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        evento_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(evento_serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Evento creado correctamente!'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def update(self,request, pk=None):
        if self.get_queryset(pk):
            evento_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if evento_serializer.is_valid():
                evento_serializer.save()
                return Response(evento_serializer.data, status = status.HTTP_200_OK)
            return Response(evento_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk=None):
        categoria = Evento.objects.get(pk=pk)
        if categoria:
            categoria.state = False
            categoria.save()
            return Response({'message': 'Evento eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un evento con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        