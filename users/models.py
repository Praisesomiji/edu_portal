from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('adviser', 'Adviser'),
    )
    role = models.CharField(max_length=10, choices=ROLES)

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    gpa = models.FloatField(null=True, blank=True)
    attendance_rate = models.FloatField(null=True, blank=True)

class AdviserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='adviser_profile')
    department = models.CharField(max_length=255)

