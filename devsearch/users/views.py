from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile


def login_user(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except Exception:
            print(f"\033[31m█▓▒░ Username '{username}' does not exist\033[0m")
            messages.error(request, f"Username '{username}' does not exist")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            print("\033[31m█▓▒░ Username OR password is incorrect\033[0m")
            messages.error(request, "Username OR password is incorrect")

    return render(request, 'users/login_register.html')


def logout_user(request):
    logout(request)
    messages.info(request, "User was successfully logged out")
    return redirect('login')


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, 'users/profiles.html', context)


def user_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skills = profile.skill_set.exclude(description__exact="")  #exclude skills w/o description
    other_skills = profile.skill_set.filter(description="")
    context = {
        "profile": profile,
        "top_skills": top_skills,
        "other_skills": other_skills,
    }
    return render(request, 'users/user-profile.html', context)
