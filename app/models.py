from django.db import models


# Create your models here.

class Employee(models.Model):

    employee_name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='pics')
    designation = models.CharField(max_length=150)
    qualification = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    remarks = models.TextField(default='')
    salary = models.IntegerField()
    Status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    phone = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.employee_name