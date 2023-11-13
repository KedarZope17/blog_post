from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
import json
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            messages.success(request, f"Account successfully created for {user_name}!")
            return redirect('blog_home')
        else:
            user_name = form.cleaned_data.get('username')
            messages.error(request, f"Regrettably, account was not created for {user_name}. Please try again")
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})    
