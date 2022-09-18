from operator import mod
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feedemp(models.Model):

    fname = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    date_time = models.DateTimeField()
    feed = models.TextField(max_length=200)

    def __str__(self):
        return self.fname + " - " + self.feed

class taskAllocA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    date = models.DateField()
    time = models.TimeField()
    username = models.CharField(max_length=20)
    task = models.TextField(max_length=200)

    def __str__(self):
        return self.username

class ShiftDept(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    shift = models.CharField(max_length= 35)
    dept = models.CharField(max_length= 80)

    def __str__(self):
        return self.dept + " - " + self.shift
