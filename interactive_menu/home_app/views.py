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


def details(request,id):
    context={
        'item': Item.objects.get(id=id),
    }
    return render(request, 'details.html',context)



def home(request):
    context = {
        'breakfast' : getcategory('breakfast'),
        'drinks' : getcategory('drinks'),
        'maindishes' : getcategory('maindishes'),
        'desserts' : getcategory('desserts'),
        'sheesha' : getcategory('sheesha'),
        'salads' : getcategory('salads'),
        'allitem' : getallitem(),
    }
    return render(request, 'homeTemp.html',context)


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
            return redirect('/login')
        elif len(errors) == 0:
            request.session['userEmail'] = request.POST['email']
            return redirect('/welcome')
    return redirect('/welcome')


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
    return redirect('/loginandreg/')


def welcome(request):
    
    return render(request,'slide_page.html')

def logout(request):
    if 'userEmail' in request.session:
        request.session.clear()
        return redirect('/loginandreg/')
    return redirect('/loginandreg/')

def addcart(request, id):
    request.POST['quantity']

    thisuser = User.objects.get(email=request.session['userEmail'])
    thisitem = Item.objects.get(id=id)
    thecart = Cart.objects.create(
        user=thisuser, quantity=request.POST['quantity'])
    thecart.item.add(thisitem)
    return redirect('/home/')

def cart (request):
    cart= Cart.objects.all()
    
    sum=0
    for i in cart:
        item=Item.objects.all()
        sum+=(i.item.price * i.quantity)
    contaxt={
        'cart': Cart.objects.all(),
        'total':sum,
    }
    return render (request, 'cart.html',contaxt)   


def sendfeedback(request):
    Feedback.objects.create(description=request.POST['description'])
    return redirect('/cart/')


def admin(request):
    context = {
        "date": strftime("%d %b, %y", gmtime()),
        "time": time.strftime("%H:%M  %p", time.localtime())}
    return render(request, 'admin.html', context)
