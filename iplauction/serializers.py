from rest_framework import serializers
from .models import Team, Player


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('player_id', 'player_name', 'category', 'country', 'base_price', 'xp', 'sold', 'team')


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('team_id', 'team_name', 'budget')


class TeamDataSerializer(serializers.HyperlinkedModelSerializer):
    players = PlayerSerializer(many = True)

    class Meta:
        model = Team
        fields = ('team_id', 'team_name', 'budget', 'players')
