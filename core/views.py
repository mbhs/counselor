from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    #Render links IN ORDER!
    return render(request,"core/home.html",{"objects":TextPage.objects.order_by('numId')})

def processFile(request):
    file = request.FILES["file"]
    File(file=file).save()
    return HttpResponseRedirect(reverse("core:index"))
