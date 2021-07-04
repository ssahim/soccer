# Generated by Django 3.2.4 on 2021-06-18 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
        ('match', '0002_auto_20210618_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='guest_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='guest_team', to='team.team'),
        ),
        migrations.AlterField(
            model_name='match',
            name='host_team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='host_team', to='team.team'),
        ),
    ]