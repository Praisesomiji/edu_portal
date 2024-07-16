from django.db import models
from users.models import User

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    instructor_name = models.CharField(max_length=255)

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    current_grade = models.FloatField(null=True, blank=True)
    attendance_rate = models.FloatField(null=True, blank=True)
