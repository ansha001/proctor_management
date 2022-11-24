from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FacultyRegistrationForm

def facultyhome(request):
    return render(request, 'faculty/home.html')

def facultylogin(request):
    return render(request, 'faculty/login.html')

def facultyregister(request):
    if request.method == 'POST':
        form = FacultyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('faculty-home')

    form = FacultyRegistrationForm()
    return render(request, 'faculty/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'faculty/profile.html')