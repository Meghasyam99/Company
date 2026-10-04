from django.db import models

# Create your models here.

class EmployeeDetails(models.Model):
    name=models.CharField(max_length=30)
    username=models.CharField(max_length=45)
    password=models.CharField(max_length=150)
    salary=models.IntegerField()
    department=models.CharField(max_length=50)

    def __str__(self):
        return self.name