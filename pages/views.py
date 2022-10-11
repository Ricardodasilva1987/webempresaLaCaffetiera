from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def pages(request,page_id):
    #page = Page.objects.get(id = page_id)
    page=get_object_or_404(Page,id=page_id)
    return render(request,'pages/sample.html',{'page':page})