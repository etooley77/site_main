# Generated by Django 4.2.4 on 2023-11-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_forums', '0021_song_upload_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]