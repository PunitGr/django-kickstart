from django.contrib import admin
from .models import Player, Team


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id', 'player_name', 'category', 'team')


admin.site.register(Player, PlayerAdmin)
admin.site.register(Team)
