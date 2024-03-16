from django.contrib.auth import authenticate, logout, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserSignUpForm, UserLoginForm


# Create your views here.

def sign_up(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index:index')
    else:
        form = UserSignUpForm()
    return render(request, 'user/sign_up.html', {'form': form})


def login_to(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index:index')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form': form})


def logout_from(request):
    try:
        logout(request)
        return redirect('index:index')
    except Exception as e:
        return HttpResponse("An error occurred: " + str(e))
