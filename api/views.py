from .serializer import filmeSerializer
from .models import filmes
from rest_framework import  generics

# Create your views here.
class filmesCreate(generics.ListCreateAPIView):
    queryset = filmes.objects.all()
    serializer_class = filmeSerializer

class filmesalteracion(generics.RetrieveUpdateDestroyAPIView):
    queryset = filmes.objects.all()
    serializer_class = filmeSerializer
    lookup_field = 'pk'


