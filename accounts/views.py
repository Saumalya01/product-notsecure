from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import SignUpForm, SignInForm
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

def home(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return redirect('signin')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                return redirect('dashboard')
            except IntegrityError:
                messages.error(request, 'An account with this email already exists. Please use a different email or sign in.')
                return redirect('signup')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Rest of your views remain the same...
def signin(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignInForm()
    return render(request, 'accounts/signin.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'user': request.user})