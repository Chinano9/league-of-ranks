from django.db import models
from django.contrib.auth.models import User
import requests

# Create your models here.

class Ranking(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User)

class Summoner(models.Model):
    summonerId = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=30)
    win_rate = models.FloatField()
    rank = [ 
            'iron',
            'bronze',
            'silver',
            'gold',
            'platinum',
            'diamond',
            'master',
            'grandmaster',
            'challenger'
        ]
    ranking = models.CharField(max_length=15, choices=rank)
    division = models.CharField(max_length=1)
    league_points = models.IntegerField()

class SummonerRanking(models.Model):
    ranking = models.ForeignKey(Ranking)
    summonerId = models.ForeignKey(Summoner) 
