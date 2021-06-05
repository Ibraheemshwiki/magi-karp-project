from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from time import gmtime, strftime
import time

def main(request):
    return render(request,'home.html')

def index(request):
    if 'userEmail' in request.session:
        return redirect('/welcome/')
    if 'signin' not in request.session and 'signup' not in request.session:
        request.session['signin'] = 'block'
        request.session['signup'] = 'none'
    return render(request, 'loginAndreg.html')


def details(request):
    return render(request, 'details.html')



def home(request):
    context = {
        'breakfast' : getcategory('breakfast')

    }

    return render(request, 'homeTemp.html',context)

def cart (request):
    return render (request, 'cart.html')   

def contact (request):
    return render (request, 'contact.html')



def registration(request):
    if 'userEmail' in request.session:

        return redirect('/welcome/')
    if request.method == 'POST':
        request.session['signup'] = 'block'
        request.session['signin'] = 'none'
        errors = create_user(request.POST)
        
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/login/')
        elif len(errors) == 0:
            request.session['userEmail'] = request.POST['email']
            return redirect('/welcome/')
    return redirect('/welcome/')


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
            return redirect('/login/')
        elif len(errors) == 0:
            request.session['userEmail'] = request.POST['email']
            return redirect('/welcome/')


def welcome(request):
    
    return render(request,'slide_page.html')










def admin(request):
    context = {
        "date": strftime("%d %b, %y", gmtime()),
        "time": time.strftime("%H:%M  %p", time.localtime())}
    return render(request, 'admin.html', context)
