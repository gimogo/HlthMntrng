from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .views import PatientListView, DoctorListView, PatientUpdateView

urlpatterns = [
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('profile/', views.profile, name = 'profile'),
    path('docedit/', views.edit_doctor_profile, name = 'docedit'),
    path('patedit/', views.edit_patient_profile, name = 'patedit'),
    path('prescriptionrequest/', views.prescription_request, name = 'prescription_request'),
    path('patients/', PatientListView.as_view(), name = 'patients'),
    path('doctors/', DoctorListView.as_view(), name = 'doctors'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name = 'patient-update'),
]
