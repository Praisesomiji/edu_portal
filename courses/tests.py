from django.test import TestCase
from .models import Course, Enrollment
from users.models import User

class CourseModelTests(TestCase):
    def setUp(self):
        self.course = Course.objects.create(course_name='Django Basics', instructor_name='John Doe')
        self.student = User.objects.create_user(username='student_user', password='testpass123', role='student')

    def test_course_creation(self):
        self.assertEqual(self.course.course_name, 'Django Basics')
        self.assertEqual(self.course.instructor_name, 'John Doe')

    def test_enrollment_creation(self):
        enrollment = Enrollment.objects.create(student=self.student, course=self.course, current_grade=85, attendance_rate=90)
        self.assertEqual(enrollment.student.username, 'student_user')
        self.assertEqual(enrollment.course.course_name, 'Django Basics')
        self.assertEqual(enrollment.current_grade, 85)
        self.assertEqual(enrollment.attendance_rate, 90)
