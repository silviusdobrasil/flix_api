from rest_framework import generics
from filmes.models import Filmes
from filmes.serializers import FilmesSerializer

class FilmesCreateListView(generics.ListCreateAPIView):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer

class FilmesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filmes.objects.all()
    serializer_class = FilmesSerializer
