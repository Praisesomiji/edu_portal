from django.core.management.base import BaseCommand
# from django.contrib.auth import get_user_model
from ...models import User

class Command(BaseCommand):
    help = 'Create demo users'

    def handle(self, *args, **kwargs):
        if not User.objects.filter(username='student_user').exists():
            User.objects.create_user(username='student_user', password='testpass123', role='student')
            self.stdout.write(self.style.SUCCESS('Successfully created student user'))
        
        if not User.objects.filter(username='adviser_user').exists():
            User.objects.create_user(username='adviser_user', password='testpass123', role='adviser')
            self.stdout.write(self.style.SUCCESS('Successfully created adviser user'))
