# Generated by Django 4.2.4 on 2023-11-04 01:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site_forums', '0005_alter_post_username_delete_userpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
