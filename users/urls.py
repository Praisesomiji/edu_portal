from django.urls import path
from .views import index, register, login_view, logout_view, student_dashboard, adviser_dashboard

urlpatterns = [
    path('', index, name='index'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('student_dashboard/', student_dashboard, name='student_dashboard'),
    path('adviser_dashboard/', adviser_dashboard, name='adviser_dashboard'),
]
