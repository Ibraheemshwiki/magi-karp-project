from django.urls import path
from . import views

urlpatterns = [
    path('',views.admin),
    path('delete/<int:id>',views.delete),
]