# Generated by Django 3.2 on 2021-04-17 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YoutubeApis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtubevideos',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='youtubevideos',
            name='thumbnails',
            field=models.JSONField(blank=True),
        ),
    ]
