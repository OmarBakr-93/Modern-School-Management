from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Student, ClassModel, Grade, Attendance

admin.site.register(Student)
admin.site.register(ClassModel)
admin.site.register(Grade)
admin.site.register(Attendance)
