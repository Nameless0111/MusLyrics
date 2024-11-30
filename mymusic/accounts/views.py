from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth.models import User

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/signup.html', {'form': form})