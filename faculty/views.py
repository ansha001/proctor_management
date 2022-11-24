from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import FacultyRegistrationForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

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


def success(request):
    email = EmailMessage(
        'Profile Creation Successful',
        render_to_string('faculty/success.html'),
        settings.EMAIL_HOST_USER,
        [request.user.email],  
    )
    email.fail_silently = False
    email.send()
    user = request.user
    context = {'user': user}
    return render(request, 'faculty/success.html',context)

