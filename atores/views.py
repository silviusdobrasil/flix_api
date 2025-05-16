from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from atores.models import Atores
from atores.serializers import AtoresSerializer
from app.permissions import  GlobalDefaultPermission


class AtoresCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Atores.objects.all().order_by('nome')
    serializer_class = AtoresSerializer


class AtoresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Atores.objects.all().order_by('nome')
    serializer_class = AtoresSerializer