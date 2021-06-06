from django.urls import path
from . import views

urlpatterns = [
    path('',views.main),
    path('loginandreg/', views.index),
    path('details/<int:id>/', views.details),
    path('admin', views.admin),
    path('logout/',views.logout),
    path('cart/', views.cart),
    path('contact/', views.contact),
    path('register/', views.registration),
    path('login/', views.log_in),
    path('home/', views.home),
    path('welcome/',views.welcome),
    path('addcart/<int:id>/',views.addcart),
    path('sendfeedback/',views.sendfeedback),
    path('/submit_order', views.submit_order),
]
