# Generated by Django 3.1 on 2020-09-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20200908_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentsContacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_name', models.CharField(max_length=50)),
                ('comment_text', models.CharField(max_length=200)),
            ],
        ),
    ]
