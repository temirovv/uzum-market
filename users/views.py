from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from django.contrib.auth import login, logout

from .forms import UserForm


def register(request):
    if request.method == 'GET':
        context = {
            'form': UserForm()
        }
        return render(request, 'users/register.html', context=context)

    elif request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
        
        return render(request, 'users/register.html', context={'form': UserForm()})



def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        return render(request, 'users/login.html', context={'boshqacha_login': form})

    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('product_list')

        return render(request, 'users/login.html', context={'boshqacha_login': form})



def logout_view(request):
    logout(request)
    return redirect('product_list')
