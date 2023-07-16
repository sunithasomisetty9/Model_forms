from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    TMFO=TopicModelForm()
    d={'TMFO':TMFO}

    if request.method=='POST':
        TMFOD=TopicModelForm(request.POST)
        if TMFOD.is_valid():
            TMFOD.save()
            return HttpResponse("Insertion of data is done successfully")
        
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WMFO=WebpageModelForm()
    d={'WMFO':WMFO}

    if request.method=='POST':
        WMFOD=WebpageModelForm(request.POST)
        if WMFOD.is_valid():
            WMFOD.save()
            return HttpResponse("Insertion of data is done successfully")
        else:
            return HttpResponse('invalid data')

    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    ARMFO=AccessRecordModelForm()
    d={'ARMFO':ARMFO}

    if request.method=='POST':
        ARMFOD=AccessRecordModelForm(request.POST)
        if ARMFOD.is_valid():
            ARMFOD.save()
            return HttpResponse("Insertion of data is done successfully")

    return render(request,'insert_accessrecord.html',d)