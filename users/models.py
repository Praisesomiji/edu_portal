from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('adviser', 'Adviser'),
    )
    # Add a role field with choices set to the ROLES tuple
    role = models.CharField(max_length=10, choices=ROLES)
    # Override the groups and user_permissions fields to provide unique related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    adviser = models.ForeignKey("AdviserProfile", on_delete=models.SET_NULL, null=True, related_name='students')
    gpa = models.FloatField(null=True, blank=True)
    attendance_rate = models.FloatField(null=True, blank=True)

class AdviserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='adviser_profile')
    department = models.CharField(max_length=255)

