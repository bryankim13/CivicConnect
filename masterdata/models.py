from django.db import models

import uuid

import datetime


class Emailtemplate(models.Model):
    title = models.CharField(max_length = 200)
    shortDescription = models.CharField(max_length = 100)
    contentTemp = models.TextField()
    subject = models.CharField(max_length = 200)
    state = models.CharField(max_length = 50)
    published = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

