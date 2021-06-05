from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('details', views.details),
    path('admin', views.admin),
    path('register/', views.registration),
    path('login/', views.log_in),
    path('home/', views.home),


]
