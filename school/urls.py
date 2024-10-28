from django.urls import path, include
from . import views

app_name = 'school'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.add_student, name='students'),
    path('classes/', views.add_class, name='classes'),
    path('grades/', views.add_grade, name='grades'),
    path('attendance/', views.add_attendance, name='attendance'),
    
]
