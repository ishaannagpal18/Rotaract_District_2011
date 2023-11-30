from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from App_Login.models import *

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'aboutus.html')

def team(request):
    return render(request, 'team.html')

def projects(request):
    return render(request, 'projects.html')

def gallery(request):
    return render(request, 'gallery.html')

@login_required(login_url='/account/login')
def user_profile(request):
    return render(request, 'user_profile.html')
