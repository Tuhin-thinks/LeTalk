

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.db import models

f = FileSystemStorage(location='/media')

def index(request):
    return render(request, 'chat/index.html')
    # template = loader.get_template('chat/index.html')
    # return HttpResponse(template.render())

def login(request):
    template = loader.get_template('chat/login.html')
    return HttpResponse(template.render())

def register(request):
    if request.method == "POST":
        # pass POST data to form validation class from  here.
        print(request.POST)
        return render(request, 'chat/login.html')
    else:
        return render(request, 'chat/register.html')

def profile(request):
    template = loader.get_template('chat/profile.html')
    return HttpResponse(template.render())