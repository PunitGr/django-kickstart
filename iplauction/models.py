from __future__ import unicode_literals

from django.db import models



class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    base_price = models.FloatField(default=100000)
    xp = models.IntegerField(default=None)
    sold = models.BooleanField(default=False)
    sold_to = models.OneToOneField(Team)


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=20)
    budget = models.FloatField(default=200000000)
    player_list = models.ForeignKey(Player)
