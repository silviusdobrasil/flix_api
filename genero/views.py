from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from genero.models import Genero
from genero.serializers import GeneroSerializer
from app.permissions import GlobalDefaultPermission


class GenereCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genero.objects.all().order_by('nome')
    serializer_class = GeneroSerializer


class GeneroRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Genero.objects.all().order_by('nome')
    serializer_class = GeneroSerializer