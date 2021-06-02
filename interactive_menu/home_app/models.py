from django.db import models
import re     
# whats this for ??
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        email_ex=User.objects.filter(email=postData['email']).exists()
        if(email_ex):
            errors['email'] = "Email Already in use"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password description should be at least 8 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password =models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Feedback(models.Model):
    description = models.TextField
    uploaded_by =models.ForeignKey(User,related_name="feedback_uploaded",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user =models.ForeignKey(User,related_name="cart",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Item(models.Model):
    name = models.CharField(max_length=45)
    price= models.IntegerField()

class Order(models.Model):
    cart =models.ForeignKey(Cart,related_name="order",on_delete=models.CASCADE)
    users_who_like= models.ManyToManyField(User,related_name="liked_thoughts")
