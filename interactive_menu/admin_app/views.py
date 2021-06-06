from time import gmtime, strftime
<<<<<<< HEAD
from django.shortcuts import render
=======
from django.shortcuts import redirect, render
>>>>>>> 917680c7787b2968fa60af57487dfa39748f4850
from .models import *
import time



def admin(request):
    
    context={
        'feedback': Feedback.objects.all(),
        'order':Order.objects.all(),
        "date": strftime("%d %b, %y", gmtime()),
        "time": time.strftime("%H:%M  %p", time.localtime())
    }

    return render(request,'Admin.html',context)
<<<<<<< HEAD
=======

def delete(request,id):
    thisorder=Order.objects.get(id=id)
    thisorder.delete()
    return redirect('/admin/')
>>>>>>> 917680c7787b2968fa60af57487dfa39748f4850
