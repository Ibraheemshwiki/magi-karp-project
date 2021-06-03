from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
<<<<<<< HEAD
    path('details', views.details),
    path('admin', views.admin),
=======
    path('register/', views.registration),
    path('login/', views.log_in),

>>>>>>> f9ce6af19917ac9add32efccf1c0041d614921ad

]
