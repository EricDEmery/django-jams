from django.db import models

# Create your models here.

class Songs(models.Model):
    title = models.CharField(max_length=200)
    artist = models.ManyToManyField('Artists')
    album = models.CharField(max_length=200)
    genre = models.ManyToManyField('Genres')

    def __str__(self):
        return self.title

class Artists(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Albums(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class Genres(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label

class Users(models.Model):
    email = models.CharField(max_length=200)
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username