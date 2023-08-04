from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Songs
        fields = "__all__"

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = "__all__"

class AlbumsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Albums
        fields = "__all__"

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = "__all__"

class UsersSerializer(serialezirs.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

