from django.db import models

# Create your models here.

class Animes(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=100, blank=True, null=True)
    media = models.CharField(max_length=10, blank=True, null=True)
    episodes = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    members = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    season = models.CharField(max_length=30, blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'animes'

    def __str__(self):
        return self.title



class AnimeTest(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    genres = models.CharField(max_length=100, blank=True, null=True)
    media = models.CharField(max_length=10, blank=True, null=True)
    episodes = models.IntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    members = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    season = models.CharField(max_length=20, blank=True, null=True)
    source = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'anime_test'

    def __str__(self):
        return self.title