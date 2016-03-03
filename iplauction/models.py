from __future__ import unicode_literals

from django.db import models


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=20)
    budget = models.FloatField(default=200000000)

    def __str__(self):
        return self.team_name

    def budget_return(self):
        return self.budget


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=50)
    category = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    base_price = models.FloatField(default=100000)
    xp = models.IntegerField(default=None)
    sold = models.BooleanField(default=False)
    team = models.ForeignKey(Team, null=True, blank=True)

    def __str__(self):
        return self.player_name
