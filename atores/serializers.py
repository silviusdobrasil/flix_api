from rest_framework import serializers
from atores.models import Atores

class AtoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atores
        fields = '__all__'