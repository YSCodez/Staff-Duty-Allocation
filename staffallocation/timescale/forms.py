from curses.ascii import EM
from django import forms
from django.forms import ModelForm
from .models import Feedemp

#Create a Employee Form
class EmployeesForm(ModelForm):
    class Meta:
        model = Feedemp
        feilds = ('fname', 'email', 'date_time', 'feed')