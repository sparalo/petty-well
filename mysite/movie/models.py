from django.db import models

# Create your models here.
class Movie(models.Model):
    backdrop_path = models.CharField(max_length=200)
    first_air_date = models.CharField(max_length=200)
    genre_ids = models.IntegerField()
    id = models.Field(primary_key = True)
    name = models.CharField(max_length=200)
    origin_country = models.CharField(max_length=200)
    original_language = models.CharField(max_length=200)
    origin_name = models.CharField(max_length=200)
    overview = models.CharField(max_length=300)
    popularity = models.IntegerField()
    poster_path = models.CharField(max_length=200)
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
