from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

# Create your views here.

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('profile')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', { 'form': form })


@login_required(login_url='/accounts/login')
def profile_view(request):
    return render(request, 'users/profile.html')
