# Generated by Django 3.1 on 2020-09-08 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_commentscontacts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentscontacts',
            old_name='comment_name',
            new_name='comment_name_1',
        ),
        migrations.RenameField(
            model_name='commentscontacts',
            old_name='comment_text',
            new_name='comment_text_1',
        ),
    ]
