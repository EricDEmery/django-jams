from django.db import models

# Create your models here.

class Songs(models.Model):
    title = models.Charfield(max_length=200)
    artist = models.ManyToManyField('Artists')
    album = models.Charfield(max_length=200)
    genre = models.ManytoManyfield('Genres')

    def __str__(self):
        return self.title

class Artists(models.Model):
    name = models.Charfield(max_length=200)

    def __str__(self):
        return self.name

class Albums(models.Model):
    label = models.Charfield(max_length=200)

    def __str__(self):
        return self.label

class Genres(models.Model):
    label = models.Charfield(max_length=200)

    def __str__(self):
        return self.label