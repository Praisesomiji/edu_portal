from django.db import models
from users.models import User
from courses.models import Course

class Grade(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grades')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grades')
    grade = models.FloatField()
    date_recorded = models.DateTimeField(auto_now_add=True)
