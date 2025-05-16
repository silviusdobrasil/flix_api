from rest_framework import generics
from genero.models import Genero
from genero.serializers import GeneroSerializer


class GenereCreateListView(generics.ListCreateAPIView):
    queryset = Genero.objects.all().order_by('nome')
    serializer_class = GeneroSerializer


class GeneroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genero.objects.all().order_by('nome')
    serializer_class = GeneroSerializer