from django.db.models import Avg
from rest_framework import serializers
from filmes.models import Filmes

class FilmesSerializer(serializers.ModelSerializer):

    media_avaliacoes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Filmes
        fields = '__all__'

    def get_media_avaliacoes(self, obj):
        notas = obj.avaliacoes.aggregate(Avg('nota'))['nota__avg']

        if notas:
            return round(notas, 2)
        
        return None

    
    def validate_data_lancamento(self, value):

        if value.year <= 2000:
            raise serializers.ValidationError("O ano de lançamento deve ser maior ou igual a 2000.") 
        return value
    
    def validate_resumo(self, value):

        if len(value) > 200:
            raise serializers.ValidationError('O campo resumo deve ter no máximo 200 caracteres') 
        return value
    