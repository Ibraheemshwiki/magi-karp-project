
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from time import gmtime, strftime
import time


def index(request):
    if 'signin' not in request.session and 'signup' not in request.session:
        request.session['signin'] = 'block'
        request.session['signup'] = 'none'

# Create your views here.


def details(request):
    return render(request, 'details.html')


def admin (request):
    context = {
            "date": strftime("%d %b, %y", gmtime()),
            "time": time.strftime("%H:%M  %p", time.localtime())}
    return render (request, 'admin.html', context)

def registration(request):
    if 'userEmail' in request.session:

        return redirect('/welcome/')
    if request.method == 'POST':
        request.session['signup'] = 'block'
        request.session['signin'] = 'none'
        errors = create_user(request.POST)
        # if no errors it will create new user
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        elif len(errors) == 0:
            request.session['userEmail'] = request.POST['email']
            return redirect('/')
    return redirect('/')


def log_in(request):
    if 'userEmail' in request.session:
        return redirect('/welcome/')
    if request.method == 'POST':
        request.session['signin'] = 'block'
        request.session['signup'] = 'none'
        errors = check_email(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        elif len(errors) == 0:
            request.session['userEmail'] = request.POST['email']
            return redirect('/')