from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, UpdateProfileForm, UpdatePasswordForm
from django.contrib.auth.models import User

# Register View
def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Registration successful! You can now log in.")
            return redirect('signin')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome, {user.username}')
                return redirect('profile')
            else:
                messages.error(request, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'signin.html', {'form': form})

# Logout View
@login_required(login_url='signin')
def signout(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('signin')

# Profile View
@login_required(login_url='signin')
def profile(request):
    return render(request, 'profile.html')

# Update Profile
@login_required(login_url='signin')
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        form = UpdateProfileForm(instance=request.user)
    return render(request, 'update_profile.html', {'form': form})

# Update Password
@login_required(login_url='signin')
def update_password(request):
    if request.method == 'POST':
        form = UpdatePasswordForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password got updated')
            return redirect('profile')
    else:
        form = UpdatePasswordForm(user=request.user)
    return render(request, 'update_password.html', {'form': form})
