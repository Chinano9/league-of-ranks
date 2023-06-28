from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Ranking(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Summoner(models.Model):
    summonerId = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=30)
    win_rate = models.FloatField()
    rank = [ 
            ('ir','iron'),
            ('br','bronze'),
            ('sl','silver'),
            ('gl','gold'),
            ('pl','platinum'),
            ('di','diamond'),
            ('ms','master'),
            ('gm','grandmaster'),
            ('ch','challenger')
        ]
    ranking = models.CharField(max_length=15, choices=rank)
    division = models.CharField(max_length=1)
    league_points = models.IntegerField()
    profile_icon = models.CharField(max_length = 10)

class SummonerRanking(models.Model):
    ranking = models.ForeignKey(Ranking, on_delete=models.CASCADE)
    summonerId = models.ForeignKey(Summoner, on_delete=models.CASCADE) 
