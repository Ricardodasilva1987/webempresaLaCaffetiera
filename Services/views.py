from django.shortcuts import render
from .models import *

# Create your views here.

def servicio(request):
    services = Service.objects.all()

    return render(request,'Services/services.html',{'services':services})