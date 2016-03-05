from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


class Team(models.Model):
    team_id = models.IntegerField(primary_key=True)
    team_name = models.CharField(max_length=20)
    budget = models.FloatField(default=200000000)
    slug = models.SlugField(default='', blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.team_name)
            x =1
            temp_slug = self.slug
            while True:
                if not Team.objects.filter(slug=temp_slug).exists():
                    break
                temp_slug = "%s-%d" % (self.slug, x)
                x += 1
            self.slug = temp_slug
            super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.team_name

    def budget_return(self):
        return self.budget


class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True, null=True)
    category = models.CharField(max_length=20)
    country = models.CharField(max_length=30)
    base_price = models.FloatField(default=100000)
    xp = models.IntegerField(default=None)
    sold = models.BooleanField(default=False)
    team = models.ForeignKey(Team, null=True, blank=True, related_name='players')

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.player_name)
            x = 1
            temp_slug = self.slug
            while True:
                if not Player.objects.filter(slug=temp_slug).exists():
                    break
                temp_slug = "%s-%d" % (self.slug, x)
                x += 1
            self.slug = temp_slug      
        super(Player, self).save(*args, **kwargs)

    def __str__(self):
        return self.player_name
