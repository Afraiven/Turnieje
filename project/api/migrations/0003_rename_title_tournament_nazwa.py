# Generated by Django 3.2.14 on 2023-01-04 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_player_team'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tournament',
            old_name='title',
            new_name='nazwa',
        ),
    ]
