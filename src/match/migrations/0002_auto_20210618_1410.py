# Generated by Django 3.2.4 on 2021-06-18 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='score',
        ),
        migrations.AddField(
            model_name='match',
            name='guest_team',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_team', to='team.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='guest_team_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='host_team',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_team', to='team.team'),
        ),
        migrations.AddField(
            model_name='match',
            name='host_team_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='match_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
