from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200, unique=True)
    biography = models.TextField(blank=True, null=True)
    songs = models.ManyToManyField('songs.Song', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/authors/{self.name}/"