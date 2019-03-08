from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has successfully been created .. now you can log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', context={'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(request, f'Your Profile has been updated')
            return redirect('profile')
        else:
            p_form = ProfileUpdateForm(instance=request.user.profile)
            u_form = UserUpdateForm(instance=request.user)
            print("form data are not valid")
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'users/profile.html', {'p_form': p_form, 'u_form': u_form})
