from django.shortcuts import render, redirect
from .forms import StudentForm, ClassForm, GradeForm, AttendanceForm


# school/views.py
from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Student, ClassModel, Grade, Attendance

# school/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Adjust the template name/path as needed


def dashboard(request):
    # Your logic for the dashboard goes here
    return render(request, 'dashboard.html')  # Adjust the template name/path as needed



def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    else:
        form = StudentForm()
    return render(request, 'students.html', {'form': form})

def add_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('classes')
    else:
        form = ClassForm()
    return render(request, 'classes.html', {'form': form})

def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades')
    else:
        form = GradeForm()
    return render(request, 'grades.html', {'form': form})

def add_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance')
    else:
        form = AttendanceForm()
    return render(request, 'attendance.html', {'form': form})
