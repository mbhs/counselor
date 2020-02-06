from django.db import models
from django.utils import timezone

# Create your models here.
class TextPage(models.Model):
    title = models.CharField(max_length=200)
    shortTitle = models.CharField(max_length=200)
    content = models.TextField()
    numId = models.IntegerField()
    def __str__(self):
        return self.shortTitle

    
class Event(models.Model):
    date = models.DateTimeField()
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title

class GoogleDriveAttachment(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    description = models.TextField()
    def __str__(self):
        return self.name

class File(models.Model):
    file = models.FileField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    def __str__(self):
        return self.file.url

class Announcement(models.Model):
    text = models.TextField(blank=True)
    date = models.DateTimeField()
    def __str__(self):
        return self.text

class Counselor(models.Model):
    last = models.CharField(max_length=200)
    first = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200,blank=True)
    alphaRange = models.CharField(max_length=200)

    bio = models.TextField(blank=True)
    hours = models.TextField(blank=True)
    interruptions = models.TextField(blank=True)

    studentEmails = models.TextField(blank=True)


    user = models.OneToOneField("auth.user",on_delete = models.SET_NULL,null=True)
    def __str__(self):
        return self.last + ", " + self.first

class CounselorAnnouncement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title
