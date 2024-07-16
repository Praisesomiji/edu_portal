from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import StudentProfile, AdviserProfile

class UserModelTests(TestCase):
    def setUp(self):
        self.user_student = get_user_model().objects.create_user(
            username='student_user',
            password='testpass123',
            role='student'
        )
        self.user_adviser = get_user_model().objects.create_user(
            username='adviser_user',
            password='testpass123',
            role='adviser'
        )
        StudentProfile.objects.create(user=self.user_student, gpa=3.5, attendance_rate=95)
        AdviserProfile.objects.create(user=self.user_adviser, department='Computer Science')

    def test_student_profile_creation(self):
        student_profile = StudentProfile.objects.get(user=self.user_student)
        self.assertEqual(student_profile.gpa, 3.5)
        self.assertEqual(student_profile.attendance_rate, 95)

    def test_adviser_profile_creation(self):
        adviser_profile = AdviserProfile.objects.get(user=self.user_adviser)
        self.assertEqual(adviser_profile.department, 'Computer Science')

from django.urls import reverse
from django.test import Client

class UserViewsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_student = get_user_model().objects.create_user(username='student_user', password='testpass123', role='student')
        self.user_adviser = get_user_model().objects.create_user(username='adviser_user', password='testpass123', role='adviser')

    def test_student_dashboard_view(self):
        self.client.login(username='student_user', password='testpass123')
        response = self.client.get(reverse('student_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/student_dashboard.html')

    def test_adviser_dashboard_view(self):
        self.client.login(username='adviser_user', password='testpass123')
        response = self.client.get(reverse('adviser_dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/adviser_dashboard.html')
