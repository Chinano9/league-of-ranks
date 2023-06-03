from django.db import models
from django.contrib.auth.models import User
import requests

# Create your models here.

class Ranking(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)

class Summoner(models.Model):
    summonerId = models.CharField(primary_key=True, max_length=50)

class SummonerRanking(models.Model):
    ranking = models.ForeignKey(Ranking)
    summonerId = models.ForeignKey(Summoner)
    position = models.IntegerField('Position in the ranking table')
