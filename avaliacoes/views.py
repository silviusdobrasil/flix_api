from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from avaliacoes.models import Avaliacoes
from avaliacoes.serializers import AvaliacaoSerializer
from app.permissions import  GlobalDefaultPermission

class AvaliacaoCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer

class AvaliacaoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Avaliacoes.objects.all()
    serializer_class = AvaliacaoSerializer

