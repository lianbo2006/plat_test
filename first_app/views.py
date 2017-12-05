from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template import Context, Template


# Create your views here.
def index(request):

    context = {}
    return render(request,'index.html',context)


def upload(request):

    context = {}
    return render(request,'upload.html',context)