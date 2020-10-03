from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import ExtendedUser

from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class ExtendedCreateUserForm(forms.ModelForm):
    class Meta:
        model = ExtendedUser
        fields = '__all__'

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'

class OrderUpdateForm(ModelForm):
	class Meta:
		model = Order
		fields = ['status','note','condition','delivery_cost']   

class paymentForm(ModelForm):
	class Meta:
		model = payment
		fields = '__all__'