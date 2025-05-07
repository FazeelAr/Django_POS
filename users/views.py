# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.contrib.auth import get_user_model

User = get_user_model()


def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        role = request.POST.get('role')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('users:register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('users:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('users:register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            role=role
        )
        user.save()
        messages.success(request, "Registration successful. Please log in.")
        return redirect('users:login')

    return render(request, 'users/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('product:product_list')  # or another view after login
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('users:login')

    return render(request, 'users/login.html')

