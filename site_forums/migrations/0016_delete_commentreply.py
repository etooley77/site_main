# Generated by Django 4.2.4 on 2023-11-14 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_forums', '0015_rename_parent_comment_commentreply_child_reply_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CommentReply',
        ),
    ]
