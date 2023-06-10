from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Summoner, SummonerRanking, Ranking
from .serializers import SummonerSerializer, SummonerRankingSerializer, RankingSerializer

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
        #if not serializer.data:
        #    pass
        return Response(serializer.data)
