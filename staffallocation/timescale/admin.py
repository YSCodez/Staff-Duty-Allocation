from re import A
from django.contrib import admin
from .models import Feedemp, taskAllocA,ShiftDept

# Register your models here.
admin.site.register(Feedemp)
admin.site.register(taskAllocA)
admin.site.register(ShiftDept)