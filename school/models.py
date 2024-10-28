from django.db import models

class ClassModel(models.Model):
    class_name = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField('Date of Birth')
    class_enrolled = models.ForeignKey(ClassModel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_model = models.ForeignKey(ClassModel, on_delete=models.CASCADE)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.student} - {self.grade}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
