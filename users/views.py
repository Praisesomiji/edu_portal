from django.shortcuts import render
from .models import User, StudentProfile
from .models import User, AdviserProfile

def student_dashboard(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    context = {
        'gpa': student_profile.gpa,
        'attendance_rate': student_profile.attendance_rate,
        'recent_grades': request.user.grades.all().order_by('-date_recorded')[:5],
        'upcoming_events': [],  # Placeholder for upcoming events logic
    }
    return render(request, 'users/student_dashboard.html', context)

def adviser_dashboard(request):
    adviser_profile = AdviserProfile.objects.get(user=request.user)
    advisees = User.objects.filter(student_profile__adviser=adviser_profile)
    context = {
        'advisees': advisees,
        'total_students': advisees.count(),
        'students_at_risk': [],  # Placeholder for students at risk logic
        'upcoming_sessions': [],  # Placeholder for upcoming sessions logic
    }
    return render(request, 'users/adviser_dashboard.html', context)
