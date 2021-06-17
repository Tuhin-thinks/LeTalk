

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.core.files.storage import FileSystemStorage
from django.db import models

from .forms import SignUpForm
from colorama import Fore

f = FileSystemStorage(location='/media')

def index(request):
    return render(request, 'chat/index.html')

def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        # print(f"{Fore.LIGHTYELLOW_EX}POST data:", dict(request.POST.items()), f"{Fore.RESET}")
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('login')
    else:
        return render(request, 'chat/login.html', {})

def user_register(request):
    print(f"{Fore.LIGHTYELLOW_EX}\tAm here!\n\tMethod:{request.method}{Fore.RESET}")
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                # print(f"\t{Fore.RED}Form validation success!{Fore.RESET}")
                form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                print(f"{Fore.RED}username:{username}, password:{password}{Fore.RESET}")
                user = authenticate(username=username, password=password)
                login(request,user)
                return redirect('/')
            else:
                print(f"\t{Fore.RED}Form validation FAILED!\nErrors:{form.errors.as_json()}{Fore.RESET}")
                return render(request, 'chat/register.html', {'regForm': form})
        else:
            form = SignUpForm()

        return render(request, 'chat/register.html', {'regForm': form})

def user_logout(request):
    logout(request)
    return redirect('/')

def profile(request):
    return render(request, 'chat/profile.html')