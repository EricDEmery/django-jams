from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import SongsSerializer, ArtistsSerializer, AlbumsSerializer, GenresSerializer, UsersSerializer
from .models import Songs, Artists, Albums, Genres, Users
# Create your views here.

class SongsViewSet(viewsets.ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongSerializer

class ArtistsViewSet(viewsets.ModelViewSet):
    queryset = Artists.objects.all()
    serializer_class = ArtistSerializer

class AlbumsViewSet(viewsets.ModelViewSet):
    queryset = Albums.objects.all()
    serializer_class = AlbumSerializer

class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer