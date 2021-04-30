from django.shortcuts import render, redirect
from .forms import UserRegisterForm, DoctorUpdateForm, PatientUpdateForm, PrescriptionRequestForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Patient, Doctor
from django.views.generic import ListView, DetailView, UpdateView

# Create your views here.

def register(request):
    if request.method == 'POST':
        u_form = UserRegisterForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            return redirect('login')
            #username = form.cleaned_data.get('username')
    else:
        u_form = UserRegisterForm()

    context = {
        'u_form' : u_form,
        'title' : 'Register',
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')


@login_required
def edit_doctor_profile(request):
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST, request.FILES, instance=request.user.doctor)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = DoctorUpdateForm(instance=request.user.doctor)

    context = {
        'title' : 'Edit Profile',
        'form' : form,
    }
    return render(request, 'users/editdocprofile.html', context)


@login_required
def edit_patient_profile(request):
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, request.FILES, instance=request.user.patient)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PatientUpdateForm(instance=request.user.patient)

    context = {
        'title' : 'Edit Profile',
        'form' : form,
    }
    return render(request, 'users/editpatprofile.html', context)


@login_required
def prescription_request(request):
    if request.method == 'POST':
        form = PrescriptionRequestForm(request.POST, instance=request.user.patient)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = PrescriptionRequestForm(instance=request.user.patient)

    context = {
        'title' : 'Prescription Request',
        'form' : form,
    }
    return render(request, 'users/prescription_request.html', context)


class PatientListView(ListView):
    model = Patient
    context_object_name = 'patients'

class DoctorListView(ListView):
    model = Doctor
    context_object_name = 'doctors'



class PatientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Patient
    fields = ['health_problem'] #form fields

    def form_valid(self, form):
        #form<this form> <set author> = current logged in user
        form.instance.user = self.request.user
        #run overridden form_valid method
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == Patient.user:
            return True
        return False
