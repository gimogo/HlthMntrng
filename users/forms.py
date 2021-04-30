from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Patient, Doctor

CHOICES=[('item1','item 1'),
         ('item2','item 2')]

class UserRegisterForm(UserCreationForm):
    #email = forms.EmailField()
    email = forms.EmailField(label = (u'Email Adress')) #for labelling

    class Meta:
        model = User
        fields = ['username', 'email', 'is_doctor' ,'is_patient' ,'password1', 'password2']


class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['specialization', 'education', 'image']

class PatientUpdateForm(forms.ModelForm):
    height = forms.FloatField(required = False, label = (u'Height (in Meters):'))
    weight = forms.FloatField(required = False, label = (u'Weight (in KG):'))
    class Meta:
        model = Patient
        fields = [ 'height', 'weight', 'image','health_problem',]


class PrescriptionRequestForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['health_problem']
