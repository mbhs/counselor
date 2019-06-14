from django.db import models

# Create your models here.
class TextPage(models.Model):
    title = models.CharField(max_length=200)
    shortTitle = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.shortTitle
