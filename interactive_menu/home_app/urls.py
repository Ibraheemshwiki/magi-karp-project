from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('details', views.details),
    path('admin', views.admin),

]
