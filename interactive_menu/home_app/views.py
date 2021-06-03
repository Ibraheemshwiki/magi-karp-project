from django.shortcuts import render
from time import gmtime, strftime
import time


def index(request):
    return render(request, 'home.html')

# Create your views here.


def details(request):
    return render(request, 'details.html')


def admin (request):
    context = {
            "date": strftime("%d %b, %y", gmtime()),
            "time": time.strftime("%H:%M  %p", time.localtime())}
    return render (request, 'admin.html', context)