from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

@user_passes_test(lambda user: not user.username, login_url='home', redirect_field_name=None)
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Username or Password is incorrect, Try again!"))
            return redirect('login')
    else:
        return render(request, 'login.html',{})


def logout_user(request):
    logout(request)
    messages.success(request, ("You were Logged Out!"))
    return redirect('home')

@user_passes_test(lambda user: not user.username, login_url='home', redirect_field_name=None)
def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,("Registration Successful!"))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, "register.html", {
        'form':form,
    })