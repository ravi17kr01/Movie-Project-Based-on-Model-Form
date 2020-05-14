from django.db import models

class Movie(models.Model):
    rdate = models.DateField()
    moviename = models.CharField(max_length = 30)
    hero = models.CharField(max_length=30)
    heroine = models.CharField(max_length = 30)
    rating = models.IntegerField()
