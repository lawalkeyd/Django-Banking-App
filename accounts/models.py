from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
    )
from decimal import Decimal
from django.conf import settings
from django.contrib.auth.models import AbstractUser
import random





class UserProfile(AbstractUser):
    # first_name = None
    # last_name = None

    username = models.CharField('username', max_length=150, unique=True, default="")
    full_name= models.CharField(max_length=50, default="",blank= False)
    password= models.CharField(max_length=200,blank=False, default="")
    birth_date = models.DateField(null=True, blank=True)
    email = models.EmailField(unique=True, blank=False)
    contact_no = models.IntegerField(unique=True ,null=True)
    Address = models.CharField(max_length=512)
    city = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    occupation = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='admin/', blank=True, null = True)
    account_id =  models.IntegerField(unique=True, default=random.randint(000000, 999999))
    balance = models.DecimalField(
        default=0,
        max_digits=12,
        decimal_places=2
    )


    USERNAME_FIELD = 'username'  # use email to log in

    def __str__(self):
        return str(self.username)
    class Meta:
        db_table = "users"


# class Accounts(models.Model):
#     user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
#     balance = models.DecimalField(
#         default=0,
#         max_digits=12,
#         decimal_places=2
#     )
#
#
#     Interest_amount = models.DecimalField(
#       decimal_places=2,
#       max_digits=12,null=True, blank=True
#       )
#     #filter all the transactions in one go
#
#
#     timestamp = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return str(self.account_no)
#


class Transactions(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE)
    Receiver_name = models.CharField(max_length=60)
    Account_number = models.IntegerField()
    Bank_name = models.CharField(max_length=120)
    Swift_code = models.IntegerField()
    country = models.CharField(max_length=104)



    amount = models.DecimalField(
      decimal_places=2,
      max_digits=12,
        null=True, blank=True
      )

    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.amount)