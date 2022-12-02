# from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import MovieSerializer
from .models import Movies
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class MovieList(generics.ListAPIView):
    queryset= Movies.objects.order_by('-created_at').all()
    serializer_class= MovieSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filtersset_fields=['category_id','release_type']
    search_fields= ['name','description']

class MovieDetail(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer
