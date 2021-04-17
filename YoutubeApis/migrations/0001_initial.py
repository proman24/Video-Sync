# Generated by Django 3.2 on 2021-04-17 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YoutubeVideos',
            fields=[
                ('video_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('publish_time', models.DateTimeField()),
                ('thumbnails', models.JSONField()),
            ],
            options={
                'db_table': 'youtube_videos',
            },
        ),
    ]