from rest_framework import serializers
from .models import Ranking, Summoner, SummonerRanking
from django.contrib.auth.models import User

class UserSerializer (serializers.Serializer):
    class Meta:
        model = User
        fields = '__all__'

class RankingSerializer(serializers.Serializer):
    class Meta:
        model = Ranking
        fields = '__all__'

class SummonerSerializer(serializers.Serializer):
    class Meta:
        model = Summoner
        fields = '__all__'

class SummonerRankingSerializer(serializers.Serializer):
    class Meta:
        model = SummonerRanking
        fields = '__all__'
