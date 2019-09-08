from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    #Render links IN ORDER!
    return render(request,"core/home.html",{"objects":TextPage.objects.order_by('numId')})


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
    return render(request,"core/calendar.html",{"objects":TextPage.objects.order_by('numId'),"events":Event.objects.order_by("date")})
