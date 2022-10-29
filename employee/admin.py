from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display =('name','image','email','joining_date','updated_date')