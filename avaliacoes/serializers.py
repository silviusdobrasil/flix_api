from rest_framework import serializers
from avaliacoes.models import Avalicoes

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avalicoes
        fields = '__all__'

