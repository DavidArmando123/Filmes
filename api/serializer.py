from rest_framework import serializers
from .models import filmes

class filmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = filmes
        fields = '__all__'

    def validate_data_de_lancamento (self, valor):
        if not isinstance(int, valor):
            raise serializers.ValidationError("Valor não inteiro")
        if valor > 1000 and valor < 2025:
            raise serializers.ValidationError("ano inválido")
        return valor 
    
    def validate(self, data):
        titulo = data.get('titulo')
        ano = data.get('ano_de_lancamento')
        if filmes.objects.filter(titulo=titulo, ano_de_lancamento=ano).exists():
            raise serializers.ValidationError("Filme já cadastrado!")
        return data


