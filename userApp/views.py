from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from .forms import LoginForm, SignUpForm
from django.contrib import messages


def login(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        login_form, signup_form = None, None
        status = 0
        if request.method == "POST":

            if request.POST.get('form-key') == 'ورود':
                login_form = LoginForm(request.POST or None)
                if login_form.is_valid():
                    user = login_form.login(request)
                    if user:
                        if user.profile.approved:
                            auth_login(request, user)
                            return redirect('index')
                messages.warning(request,
                                 'نام کاربری یا رمز عبور وارد شده، در سامانه موجود نمی باشد')

            if request.POST.get('form-key') == 'ثبت نام':
                signup_form = SignUpForm(request.POST)
                status = -1
                if signup_form.is_valid():
                    user = signup_form.save()
                    user.refresh_from_db()
                    user.profile.birth_date = signup_form.cleaned_data.get('birth_date')
                    user.profile.phone = signup_form.cleaned_data.get('phone')
                    user.profile.nationalCode = signup_form.cleaned_data.get('nationalCode')
                    messages.success(request,
                                     'مشخصات وارد شده با موفقیت در سامانه ثبت شد، منتظر تایید مدیر سامانه بمانید')
                    user.save()
                    # raw_password = signup_form.cleaned_data.get('password1')
                    # user = authenticate(username=user.username, password=raw_password)
                    # print(user)
                    # auth_login(request, user)
                    # status = 1
                    return redirect('logout')

        if status == -1:
            messages.error(request,
                           'خطا! مشخصات شما در سامانه ثبت نشد، دوباره مقادیر ورودی ها را چک نمایید')

        context = {
            'login_form': login_form,
            'signup_form': signup_form,
        }

        return render(request, 'login-register.html', context)
