from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .models import StudentProfile, AdviserProfile
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required

def index(request):
    user = request.user
    if user.is_authenticated:
        if user.role == 'student':
            return redirect('student_dashboard')
        elif user.role == 'adviser':
            return redirect('adviser_dashboard')
    return redirect('login')

#Authenticate

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'adviser':
                return redirect('adviser_dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'adviser':
                return redirect('adviser_dashboard')
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

#Render

@login_required
def student_dashboard(request):
    student_profile = StudentProfile.objects.get(user=request.user)
    context = {
        'gpa': student_profile.gpa,
        'attendance_rate': student_profile.attendance_rate,
        'recent_grades': request.user.grades.all().order_by('-date_recorded')[:5],
        'upcoming_events': [],  # Placeholder for upcoming events logic
    }
    return render(request, 'users/student_dashboard.html', context)

@login_required
def adviser_dashboard(request):
    adviser_profile = AdviserProfile.objects.get(user=request.user)
    advisees = adviser_profile.students.all()
    context = {
        'advisees': advisees,
        'total_students': advisees.count(),
        'students_at_risk': [],  # Placeholder for students at risk logic
        'upcoming_sessions': [],  # Placeholder for upcoming sessions logic
    }
    return render(request, 'users/adviser_dashboard.html', context)
