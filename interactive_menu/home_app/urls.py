from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('loginandreg/', views.index),
    path('details', views.details),
    path('admin', views.admin),
    path('chart', views.chart),
    

    path('register/', views.registration),
    path('login/', views.log_in),
    path('home', views.home),
    path('welcome/',views.welcome),

]
