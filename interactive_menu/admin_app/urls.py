from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('',views.admin)
=======
    path('',views.admin),
    path('delete/<int:id>',views.delete),
>>>>>>> 917680c7787b2968fa60af57487dfa39748f4850
]