from rest_framework import serializers
from .models import Filme, Categoria

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
       model = Categoria
       fields = '__all__'

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
       model = Filme
       fields = '__all__'