from django.db import models
import uuid

from django.utils import timezone

class Emailtemplate(models.Model):
    title = models.CharField(max_length = 200)
    shortDescription = models.CharField(max_length = 100)
    contentTemp = models.TextField()
    subject = models.CharField(max_length = 200)
    state = models.CharField(max_length = 50)
    published = bool
    user = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.title
