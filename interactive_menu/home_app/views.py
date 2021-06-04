from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def index(request):
    if 'signin' not in request.session and 'signup' not in request.session:
        request.session['signin'] = 'block'
        request.session['signup'] = 'none'

    return render(request, 'loginAndreg.html')


def home(request):

    return render(request, 'home.html')


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
