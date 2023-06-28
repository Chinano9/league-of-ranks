from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.shortcuts import get_object_or_404
from .models import Summoner, SummonerRanking, Ranking
from .serializers import SummonerSerializer, SummonerRankingSerializer, RankingSerializer
import requests
import os


"""http://ddragon.leagueoflegends.com/cdn/13.12.1/img/profileicon/685.png"""
# Create your views here.

class SummonerByNameView(APIView):
    """
    View the list of summoners by name
    """

    def get(self, request, format = None):
        """
        Returns list of summoner with similar name
        """
        summoners = [] 
        for summoner in Summoner.objects.all():
            if summoner.name.lower().find(request.name.lower()) >= 0:
                summoners.append(summoner)
        serializer = SummonerSerializer(summoners)
        if not serializer.data:
            url = f'https://la1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{request.name.lower()}'
            headers = {'X-Riot-Token': os.environ.get('RIOT_API_KEY')}
            serializer.data = requests.get(url, headers)
        #    pass
        return Response(serializer.data)

class SummonerByIdView(APIView):
    """
    View the summoner specific information by its id 
    """

    def get(self, request, format=None):
        """
        Lists all the summoner information
        """
        summoner = Summoner.get_object_or_404(request.id)
        return Response(summoner)
    def post(self, request, format=None):
        """
        Records this summoner to the database
        """

class RankingView(APIView):
    """
    Gets rankings and creates them
    """

class AddSummonerToRankingView(APIView):
    pass
