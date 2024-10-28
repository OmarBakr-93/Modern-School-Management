from django import forms
from .models import Student, ClassModel, Grade, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'dob', 'class_enrolled']  # Add any other fields necessary
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }

class ClassForm(forms.ModelForm):
    class Meta:
        model = ClassModel
        fields = ['class_name', 'teacher']  # Add any other fields necessary

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['student', 'class_model', 'grade']  # Add any other fields necessary

class AttendanceForm(forms.ModelForm):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']  # Add any other fields necessary
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
