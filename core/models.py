from django.db import models

# Create your models here.
class TextPage(models.Model):
    title = models.CharField(max_length=200)
    shortTitle = models.CharField(max_length=200)
    content = models.TextField()
    numId = models.IntegerField()
    def __str__(self):
        return self.shortTitle

    
class Event(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title


class File(models.Model):
    file = models.FileField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.file.url
