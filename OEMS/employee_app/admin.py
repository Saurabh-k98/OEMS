from django.contrib import admin
from .models import Employee, Role, Department

# django123-password,saurabh,saurabh@gmail.com
# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Role)
