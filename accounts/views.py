from django.shortcuts import render, redirect
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

from accounts.forms import CustomUserCreationForm, ProfileUpdateForm
from accounts.models import Profile

# login view function
def login_view(request):
    from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# login view function
def login_view(request):
    """ Create function for login"""
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user != None:
                login(request, user)
                return redirect("/")
            messages.error(request,"The username or password is wrong!")
        form = AuthenticationForm()
        context = {"form": form}
        return render(request, "accounts/login.html", context)
    else:
        return redirect("/")

# Logout view
@login_required(login_url="./login")
def logout_view(request):
    logout(request)
    return redirect("/")

# Register view
def register_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("/accounts/login")
            else:
                messages.error(request, "رمز عبورها با هم برابر نیستند!")
                
        form = CustomUserCreationForm()
        return render(request, "accounts/register.html", {"form": form})
    else:
        return redirect("/")
    
# Profile view
def profile_view(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        if request.method == "POST":
            form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            
            if form.is_valid():
                form.save()
                messages.success(request, "پروفایل با موفقیت بروزرسانی شد!")
        else:
            form = ProfileUpdateForm(instance=profile)
            
        context = {"profile" : profile, "form" : form}
        return render(request, "accounts/profile.html", context)
    else:
        return redirect("/")
    
# Wishlist view
def wishlist_view(request):
    return render(request, "accounts/profile-fav.html")
        
