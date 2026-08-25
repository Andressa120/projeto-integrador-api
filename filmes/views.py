from rest_framework import viewsets
from .models import Filme, Categoria
from .serializers import FilmeSerializer, CategoriaSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
   queryset = Categoria.objects.all()
   serializer_class = CategoriaSerializer

class FilmeViewSet(viewsets.ModelViewSet):
   queryset = Filme.objects.all()
   serializer_class = FilmeSerializer