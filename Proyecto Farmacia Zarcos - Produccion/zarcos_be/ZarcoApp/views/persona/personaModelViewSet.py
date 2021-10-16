from rest_framework import generics, status, viewsets
from rest_framework.response import Response


from ZarcoApp.models.persona import User
from ZarcoApp.serializers.serializersPersona import PersonaSerializer


""" Model ViewSets"""

class PersonaModelViewSet(viewsets.ModelViewSet): 
    
    serializer_class = PersonaSerializer

    def get_queryset(self, pk=None):
        if pk is not None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def list(self, request):
        persona_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(persona_serializer.data, status=status.HTTP_200_OK)

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User creado correctamente!'}, status = status.HTTP_200_OK)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    def update(self,request, pk=None):
        if self.get_queryset(pk):
            persona_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if persona_serializer.is_valid():
                persona_serializer.save()
                return Response(persona_serializer.data, status = status.HTTP_200_OK)
            return Response(persona_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request,pk=None):
        persona = User.objects.get(pk=pk)
        if persona:
            persona.state = False
            persona.save()
            return Response({'message': 'Persona eliminada correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe una persona con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        