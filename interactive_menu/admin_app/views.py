from home_app.models import Feedback, Order
from django.shortcuts import render
from .models import *

def admin(request):
    context={
        'feedback': Feedback.objects.all(),
        'order':Order.objects.all(),
    }
    return render(request,'Admin.html',context)
