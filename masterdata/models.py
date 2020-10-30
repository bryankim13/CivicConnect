from django.db import models

import uuid

import datetime

class Issue(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    state = models.CharField(max_length= 2)
    district = models.CharField(max_length= 5)
    published = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title    

class Emailtemplate(models.Model):
    title = models.CharField(max_length = 200)
    shortDescription = models.CharField(max_length = 100)
    contentTemp = models.TextField()
    subject = models.CharField(max_length = 200)
    state = models.CharField(max_length = 2)
    published = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    #issue = models.ForeignKey(Issue, on_delete=models.CASCADE, default = 'ec477b08ad804fdca6e50f5f383aeebb')
    def __str__(self):
        return self.title

class Representative(models.Model):
    name = models.CharField(max_length = 100)
    state = models.CharField(max_length= 2)
    district = models.CharField(max_length= 5)
    party = models.CharField(max_length= 50)
    email = models.CharField(max_length = 50)
    def __str__(self):
        return self.name
    


