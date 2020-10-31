from django.db import models

import uuid

import datetime


class Emailtemplate(models.Model):
    title = models.CharField(max_length = 200)
    shortDescription = models.CharField(max_length = 100)
    contentTemp = models.TextField()
    subject = models.CharField(max_length = 200)
    state = models.CharField(max_length = 2)
    published = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datecreated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

class Issue(models.Model):
    emailtemplates = models.ForeignKey(Emailtemplate, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    state = models.CharField(max_length= 2)
    district = models.CharField(max_length= 5)
    published = models.BooleanField(default=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    datecreated = models.DateTimeField(auto_now_add=True)
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
    
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length= 50)
    emailtemplates = models.ForeignKey(Emailtemplate, on_delete=models.CASCADE)
    issues = models.ForeignKey(Issue, on_delete=models.CASCADE)
    representatives = models.ForeignKey(Representative, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


