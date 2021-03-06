from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, UserProfileForm, UserProfileUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.views.decorators.csrf import csrf_exempt


def home(request):  # Home Page(domain.com)
    return render(request, 'authenticate/home.html', {})


def contact(request):  # Contact Page
    return render(request, 'authenticate/contact.html', {})


def thank_you(request): # thank you page
    return render(request, 'authenticate/thank_you.html', {})

def about(request): # about page
    return render(request, 'authenticate/about.html', {})


@csrf_exempt
def login_user(request):  # Login Page
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'login success')
            if UserProfile.objects.filter(user=user).values('country').count()== 0:
                return redirect('bolo')
            else:
                return redirect('/profile1')
        else:
            messages.error(request, f'error while login, please try again')
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def logout_user(request):  # Contact Page
    logout(request)
    messages.success(request, f'logout successful')
    return redirect('login')


@csrf_exempt
def register_user(request):  # Register Page
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form = SignUpForm(request.POST)
            form.save()
            return redirect('thank_you')
        else:
            messages.error(request, f'Please correct the error below.')
    else:
        form = SignUpForm()
    return render(request, 'authenticate/register.html', context={'form': form})


def userprofileview(request):  # Authenticated user filling the form to complete the registration
    print("country submitted")
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            pr = UserProfile()
            pr.user = User.objects.get(id=request.user.id)
            pr.Photo = form.cleaned_data['Photo']
            pr.dob = form.cleaned_data['dob']
            pr.country = form.cleaned_data['country']
            pr.State = form.cleaned_data['State']
            pr.District = form.cleaned_data['District']
            pr.phone = form.cleaned_data['phone']
            pr.save()
            messages.success(request, f'Profile has been updated successfully')
            return redirect('/profile1')
        else:
            messages.error(request, AssertionError)
    else:
        form = UserProfileForm()
    return render(request, 'authenticate/bolo.html', context={'form': form})

@login_required(login_url="/login/")
def profile_page(request):  # Fetching data from DB to show user's complete profile page
    data = get_object_or_404(UserProfile, user=request.user)
    data2 = User.objects.get(id = request.user.id)
    context = {'data': data, 'data2': data2}
    return render(request, 'authenticate/profile1.html', context)


@login_required(login_url="/login/")
def editUserProfile(request):
    if request.method == "POST":
        form = UserProfileUpdateForm(request.POST, instance=request.user)  # default user profile update
        obj = UserProfile.objects.get(user__id=request.user.id)
        form1 = UserProfileForm(request.POST or None, instance=obj)

        if form.is_valid() and form1.is_valid():
            obj.Photo = form1.cleaned_data['Photo']
            obj.dob = form1.cleaned_data['dob']
            obj.country = form1.cleaned_data['country']
            obj.State = form1.cleaned_data['State']
            obj.District = form1.cleaned_data['District']
            obj.phone = form1.cleaned_data['phone']
            form.save()
            form1.save()
            messages.success(request, f'updated successfully')
            return redirect('/profile1')
        else:
            messages.error(request, f'Please correct the error below.')
    else:
        form = UserProfileUpdateForm(instance=request.user)
        form1 = UserProfileForm(instance=request.user.profile)
    return render(request, "authenticate/editProfilePage.html", locals())


@login_required(login_url="/login/")
def passwordChange(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'updated successfully')
            return redirect('/profile1')
        else:
            messages.error(request, f'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, "authenticate/pass_edit.html", {'form': form})

