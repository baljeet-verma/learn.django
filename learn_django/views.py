
from django.http import HttpResponse
from django.shortcuts import render

from .forms import RegistrationForm

def home(request):
    return render(request, 'home.html', {'form': RegistrationForm(auto_id='register_%s')})    