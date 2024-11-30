from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    release_year = models.PositiveIntegerField(null=True, blank=True)
    album = models.CharField(max_length=200, null=True, blank=True)
    lyrics = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title