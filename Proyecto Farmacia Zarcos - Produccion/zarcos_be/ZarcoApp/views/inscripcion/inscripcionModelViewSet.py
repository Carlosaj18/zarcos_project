from rest_framework import generics, status, viewsets
from rest_framework.response import Response

from ZarcoApp.models.inscripcion import Inscripcion
from ZarcoApp.serializers.serializersInscripcion import InscripcionSerializer



""" Model ViewSets"""

class InscripcionModelViewSet(viewsets.ModelViewSet): 
    
    serializer_class = InscripcionSerializer

    def get_queryset(self, pk=None):
        if pk is not None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        inscripcion_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(inscripcion_serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Inscripcion creada correctamente!'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def update(self,request, pk=None):
        if self.get_queryset(pk):
            inscripcion_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if inscripcion_serializer.is_valid():
                inscripcion_serializer.save()
                return Response(inscripcion_serializer.data, status = status.HTTP_200_OK)
            return Response(inscripcion_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk=None):
        inscripcion = Inscripcion.objects.get(pk=pk)
        if inscripcion:
            inscripcion.state = False
            inscripcion.save()
            return Response({'message': 'Inscripcion eliminada correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una inscripcion con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        