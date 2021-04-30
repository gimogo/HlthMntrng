from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import TemplateView
def home(request):
    context = {
        'title' : 'Home',
    }
    return render(request, 'home/home.html', context)

def about(request):
    context = {
        'title' : 'About',
    }
    return render(request, 'home/about.html', context)
