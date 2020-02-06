from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import *
from .forms import *
import datetime
import pytz
# Create your views here.
def index(request):
    #Render links IN ORDER!
    return render(request,"core/home.html",{"objects":TextPage.objects.order_by('numId'),"events":Event.objects.order_by("date")})


def eventForm(request):
    if request.user == None:
        return
    return render(request,"core/addForm.html",{"objects":TextPage.objects.order_by('numId')})


def processFile(request):
    
    file = request.FILES["file"]
    File(file=file).save()
    return HttpResponseRedirect(reverse("core:index"))

def contentPage(request,st):
    return render(request,"core/content.html",{"objects":TextPage.objects.order_by('numId'),"text":get_object_or_404(TextPage,shortTitle=st )})

def listEvents(request):
    est = pytz.timezone("America/New_York")
    d = datetime.datetime.now()
    while d.weekday() != 1:
        d = d - datetime.timedelta(days=1)

    e = Event.objects.filter(date__gte=datetime.datetime.now().date())
    f = Event.objects.filter(date__gte=datetime.datetime.now().date(),date__lte=datetime.datetime.now().date()+datetime.timedelta(days=7)).order_by('date')
    g = Event.objects.filter(date__gte=d+datetime.timedelta(days=7))
    return render(request,"core/calendar.html",{"objects":TextPage.objects.order_by('numId'),"today":e,"thisWeek":e,"upcoming":g})

def counselorInfo(request, lastName):
    return HttpResponse("ok")
