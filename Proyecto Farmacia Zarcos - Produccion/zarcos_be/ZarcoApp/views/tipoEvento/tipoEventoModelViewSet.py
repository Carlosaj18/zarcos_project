from rest_framework import generics, status, viewsets
from rest_framework.response import Response


from ZarcoApp.models.tipoEve import TipoEve
from ZarcoApp.serializers.serializersTipoevento import TipoeventoSerializer


""" Model ViewSets"""

class TipoEventoModelViewSet(viewsets.ModelViewSet): 
    
    serializer_class = TipoeventoSerializer

    def get_queryset(self, pk=None):
        if pk is not None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        tipoEvento_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(tipoEvento_serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Tipo de Evento creado correctamente!'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def update(self,request, pk=None):
        if self.get_queryset(pk):
            tipoEvento_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if tipoEvento_serializer.is_valid():
                tipoEvento_serializer.save()
                return Response(tipoEvento_serializer.data, status = status.HTTP_200_OK)
            return Response(tipoEvento_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk=None):
        tipoEvento = TipoEve.objects.get(pk=pk)
        if tipoEvento:
            tipoEvento.state = False
            tipoEvento.save()
            return Response({'message': 'Tipo de Evento eliminada correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe un tipo de evento con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        