from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponse
 
def home(request):
    return render(request,'base/index.html')
