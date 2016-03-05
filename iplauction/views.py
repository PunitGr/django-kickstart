from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from iplauction.serializers import PlayerSerializer, TeamSerializer, TeamDataSerializer
from django.shortcuts import render

import json
from .models import Player, Team


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@api_view(['GET', ])
def team_list(request):
    team = Team.objects.all()
    serializer = TeamSerializer(team, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
def player_list(request):
    player = Player.objects.all()
    serializer = PlayerSerializer(player, many=True)
    return Response(serializer.data) 


@api_view(['GET', ])
def get_team_details(request, slug):
    queryset = Team.objects.get(slug=slug)
    serializer = TeamDataSerializer(queryset)
    return Response(serializer.data)


@api_view(['GET', ])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def team_details(request, slug):
    queryset = Team.objects.get(slug=slug)
    serializer = TeamDataSerializer(queryset)
    return render(request, 'team.html', {'team': json.dumps(serializer.data)})


@api_view(['GET', ])
@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
def player_profile(request, slug):
    queryset = Player.objects.get(slug=slug)
    data = {'player': queryset}
    return Response(data, template_name="player.html")
