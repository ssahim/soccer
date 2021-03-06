# Generated by Django 3.2.4 on 2021-06-27 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('match', '0003_auto_20210618_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='guest_team_players',
            field=models.ManyToManyField(related_name='host_team_player', to='player.Player'),
        ),
        migrations.AddField(
            model_name='match',
            name='host_team_players',
            field=models.ManyToManyField(related_name='guest_team_player', to='player.Player'),
        ),
    ]
