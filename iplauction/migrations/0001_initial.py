# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 16:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('player_id', models.IntegerField(primary_key=True, serialize=False)),
                ('player_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=30)),
                ('base_price', models.FloatField(default=100000)),
                ('xp', models.IntegerField(default=None)),
                ('sold', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('team_id', models.IntegerField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=20)),
                ('budget', models.FloatField(default=200000000)),
            ],
        ),
        migrations.AddField(
            model_name='player',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iplauction.Team'),
        ),
    ]