from django.shortcuts import render, redirect
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateform, ProfileUpdateform

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created!")
            return redirect('login')
        else:
            user_name = form.cleaned_data.get('username')
            messages.error(request, f"Regrettably, account was not created for {user_name}. Please try again")
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})   

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateform(request.POST, instance=request.user)
        p_form = ProfileUpdateform(
            request.POST,
            request.FILES, 
            instance=request.user.profile
        )
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            return redirect('profile')
    else:
        u_form = UserUpdateform(instance=request.user)
        p_form = ProfileUpdateform(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    
    return render(request, 'users/profile.html', context) 
