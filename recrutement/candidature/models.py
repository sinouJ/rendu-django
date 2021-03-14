from django.db import models
from django.conf import settings
from django.utils import timezone

class PostCV(models.Model):
    upload = models.FileField(upload_to='uploads/', default = 'NULL')

    def __str__(self):
        return self.title
