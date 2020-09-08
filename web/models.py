from datetime import datetime

from django.db import models


class Publication(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=datetime.now)
    text = models.TextField()


class Message(models.Model):
    user_name = models.CharField(max_length=50)
    user_phone = models.CharField(max_length=200)
    user_text = models.TextField()


class CommentsPublication(models.Model):
    comment_name = models.CharField(max_length=50)
    comment_text = models.CharField(max_length=200)


class CommentsContacts(models.Model):
    comment_name_1 = models.CharField(max_length=50)
    comment_text_1 = models.CharField(max_length=200)