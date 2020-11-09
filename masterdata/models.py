from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

import uuid
import datetime

class Emailtemplate(models.Model):
    title = models.CharField(max_length = 200)
    shortDescription = models.CharField(max_length = 100)
    contentTemp = models.TextField()
    subject = models.CharField(max_length = 200)
    state = models.CharField(max_length = 2)
    published = models.BooleanField(default=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.datecreated <= now

class Issue(models.Model):
    emailtemplates = models.ForeignKey(Emailtemplate, on_delete=models.CASCADE)
    title = models.CharField(max_length = 200)
    content = models.TextField()
    state = models.CharField(max_length= 2)
    district = models.CharField(max_length= 5)
    published = models.BooleanField(default=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.datecreated <= now

class Representative(models.Model):
    name = models.CharField(max_length = 100)
    state = models.CharField(max_length= 2)
    district = models.CharField(max_length= 5)
    party = models.CharField(max_length= 50)
    email = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

class client(models.Model):
    user = models.OneToOneField(User,related_name='clients',unique=True,null=False, db_index=True,on_delete=models.CASCADE)
    State = models.CharField(max_length = 2)
    District = models.CharField(max_length= 5, default= '')
    issues = models.ForeignKey(Issue,blank = True,null=True, on_delete=models.CASCADE)
    representatives = models.ManyToManyField(Representative)
    favorites  = models.ManyToManyField(Emailtemplate)

    def __str__(self):
        return self.user.first_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        client.objects.create(user=instance)