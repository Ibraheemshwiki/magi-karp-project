from django.db import models
import re
import bcrypt
# whats this for ??


class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        email_ex = User.objects.filter(email=postData['email']).exists()
        if(email_ex):
            errors['email'] = "Email Already in use"
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "last name should be at least 2 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be at least 8 characters"
        if postData['password'] != postData['password2']:  # aladdin add this
            errors["password2"] = " your password and confirm password should match"
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Feedback(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Category(models.Model):
    name = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




class Item(models.Model):
    name = models.CharField(max_length=45)
    category = models.ForeignKey(Category, related_name = 'items', on_delete = models.CASCADE,null=True)
    desc = models.TextField(default="descriptions about the items")
    price = models.IntegerField()
    

class Cart(models.Model):
    user = models.ForeignKey(User, related_name="cart",on_delete=models.CASCADE)
    item = models.ForeignKey(Item ,related_name='carts',on_delete=models.CASCADE,default=1)
    quantity=models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Order(models.Model):
    orderdesc=models.TextField(default=' ')
    users_who_like = models.ManyToManyField(
        User, related_name="liked_thoughts")

# creat user and validation
# by Aladdin


def create_user(data):
    dbemeil = User.objects.filter(email=data['email'])
    errors = User.objects.basic_validator(data)
    if len(dbemeil) > 0:
        errors['dbemail'] = "this email was used!"

    if len(errors) == 0:

        pw = bcrypt.hashpw(data["password"].encode(),
                        bcrypt.gensalt()).decode()
        User.objects.create(first_name=data['first_name'], last_name=data['last_name'],
                            email=data['email'], password=pw,)

    return errors


def check_email(postData):
    dbuser = User.objects.filter(email=postData['email'])
    errors = {}
    if len(dbuser) == 0:
        errors['dbemail'] = "this email not registered"
        return errors
    elif len(dbuser) > 0:
        dbpassword = dbuser.first().password
        if bcrypt.checkpw(
                postData['password'].encode(), dbpassword.encode()):
            return errors
    errors['login'] = "user name or password not valide"
    return errors

def getcategory(catname):
    return Item.objects.filter(category=Category.objects.get(name=catname))

def getallitem():
    return Item.objects.all()

def checkEmail(postemail):
    users = User.objects.filter(email=postemail)
    if len(users)>0:
        return users[0]