from django.contrib import admin
from home_app.models import Item
from home_app.models import Category
from home_app.models import User
from home_app.models import Order
from home_app.models import Cart
from home_app.models import Feedback
# Register your models here.

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Feedback)