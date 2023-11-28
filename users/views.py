from django.shortcuts import render, redirect
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm

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
    return render(request, 'users/profile.html') 
