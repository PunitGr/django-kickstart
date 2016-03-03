from django.shortcuts import render
from django.views import generic

from .models import Player, Team

class Team(generic.ListView):
    team = Team
