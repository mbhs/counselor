from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    #Render links IN ORDER!
    return render(request,"core/home.html",{"objects":TextPage.objects.order_by('numId')})
