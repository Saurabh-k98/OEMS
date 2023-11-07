from django.db import models


# Create your models here.
class Department(models.Model):
    dept = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.dept


class Role(models.Model):
    role = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.role


class Employee(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(max_length=10)
    hire_date = models.DateField()

    def __str__(self) -> str:
        return f"Name: {self.first_name} {self.last_name}, Department: {self.dept}, Role: {self.role} Contact: {self.phone}"
