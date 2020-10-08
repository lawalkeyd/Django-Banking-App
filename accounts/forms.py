from django import forms
from django.db import models
from accounts.models import UserProfile
from accounts.models import Transactions
import datetime
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
# from django.forms.extras.widgets import SelectDateWidget

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"




from .models import User


class UserRegistrationForm(UserCreationForm):
    birth_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        model = UserProfile
        fields = [
                  "username",
                  "full_name",
                  "birth_date",
                  "email",
                  "contact_no",
                  "Address",
                  "city",
                  "country",
                  "nationality",
                  "occupation",
                  "photo",
                  "password1",
                  "password2"
                  ]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control form-control-user'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-user'}),
            'contact_no': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'Address': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'city': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'password2': forms.TextInput(attrs={'class': 'form-control form-control-user'}),

        }          

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['full_name']
        user.birth_date = self.cleaned_data['birth_date']
        if commit:
            user.save()
        return user


class Deposit_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            'amount'
        ]

class Withdrawl_form(forms.ModelForm):
    class Meta:
        model = Transactions
        fields = [
            'amount', 'Receiver_name', 'Account_number', 'Bank_name', 'Swift_code', 'country'
        ]
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'Receiver_name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'Account_number': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'Bank_name': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'Swift_code': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'country': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }