from django.core.management.base import BaseCommand
# from django.contrib.auth import get_user_model
from ...models import User, StudentProfile, AdviserProfile

class Command(BaseCommand):
    help = 'Create demo users'

    def handle(self, *args, **kwargs):
        if User.objects.filter(username='adviser_user').exists():
            User.objects.filter(username='adviser_user').delete()
        adviser = AdviserProfile.objects.create(
            user=User.objects.create_user(username='adviser_user', password='testpass123', role='adviser'), 
            department="Computer Science"
        )
        self.stdout.write(self.style.SUCCESS('Successfully created adviser user'))

        if User.objects.filter(username='student_user').exists():
            User.objects.filter(username='student_user').delete()
        StudentProfile.objects.create(
            user=User.objects.create_user(username='student_user', password='testpass123', role='student'), 
            adviser=adviser
        )
        self.stdout.write(self.style.SUCCESS('Successfully created student user'))
        