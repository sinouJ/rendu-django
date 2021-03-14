from django.db import models
from django.conf import settings
from django.utils import timezone

class PostCV(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    description = models.TextField()
    fileCV = models.FileField(upload_to='uploads/', default = 'NULL')
    published_date = models.DateTimeField(blank = True, null = True)

    def __str__(self):
        return self.title
