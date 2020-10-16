from django.db import models

from django.utils import timezone

class Emailtemplate(models.Model):
    title = models.CharField(max_length = 200)
    shortDescription = models.CharField(max_length = 100)
    contentTemp = models.TextField()
    state = models.CharField(max_length = 50)
    published = bool
    def __str__(self):
        return self.title