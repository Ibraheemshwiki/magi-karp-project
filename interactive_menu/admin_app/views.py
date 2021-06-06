from time import gmtime, strftime
from django.shortcuts import redirect, render
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

def delete(request,id):
    thisorder=Order.objects.get(id=id)
    thisorder.delete()
    return redirect('/admin/')
