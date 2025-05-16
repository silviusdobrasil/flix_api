from rest_framework import generics
from avaliacoes.models import Avalicoes
from avaliacoes.serializers import AvaliacaoSerializer

class AvaliacaoCreateListView(generics.ListCreateAPIView):
    queryset = Avalicoes.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avalicoes.objects.all()
    serializer_class = AvaliacaoSerializer

