from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import LoginForm


def login(request):
    login_form = None
    if request.method == "POST":

        if request.POST.get('form-key') == 'ورود':
            login_form = LoginForm(request.POST or None)
            if login_form.is_valid():
                user = login_form.login(request)
                if user:
                    auth_login(request, user)
                    return redirect('index')

    context = {
        'login_form': login_form,
    }

    return render(request, 'login-register.html', context)
