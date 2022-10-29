
from django.db import models
import datetime
# Create your models here.
STATE = [('Madhya Pradesh','Madhya Pradesh'),('UttarPradesh','UttarPradesh'),('Gujrat',"Gujrat")]
class Employee(models.Model):
    name = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=15, null=True,blank=True)
    email = models.EmailField(max_length=100, unique=True)
    address = models.TextField(max_length=300)
    image = models.ImageField(upload_to='image/', default='a.png')
    joining_date = models.DateTimeField(auto_now_add=True,blank=True)
    updated_date = models.DateTimeField(auto_now=True,blank=True)
    city= models.CharField(max_length=50,blank=True,null=True)

    def __str__(self) :
        return self.name

    class Meta:
        verbose_name = 'EmployeeData'
        