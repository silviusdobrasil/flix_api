from rest_framework import generics
from atores.models import Atores
from atores.serializers import AtoresSerializer


class AtoresCreateListView(generics.ListCreateAPIView):
    queryset = Atores.objects.all().order_by('nome')
    serializer_class = AtoresSerializer


class AtoresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Atores.objects.all().order_by('nome')
    serializer_class = AtoresSerializer