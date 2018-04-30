from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.generic import DetailView, ListView, CreateView
from user_content.forms import UserRegisterForm, UserRegisterExtraDataForm
from . import models


# Create your views here.
def user_register(request):
    user_reg = UserRegisterForm()
    user_extra_reg = UserRegisterExtraDataForm()
    data_dict = {
        'register_form': user_reg,
        'extra_data_form': user_extra_reg,
        'registered': False,
        'passwords_not_match': False,
        'valid_data': True
    }
    if request.method == "POST":
        user_reg = UserRegisterForm(request.POST)
        user_extra_reg = UserRegisterExtraDataForm(request.POST)
        if user_reg.is_valid() and user_extra_reg.is_valid():
            temp_dict = user_reg.data
            if temp_dict['password'] != temp_dict['repeat_password']:
                data_dict['registered'] = False
                data_dict['passwords_not_match'] = True
            else:
                user = user_reg.save()
                user.set_password(user.password)
                user.save()
                print(user)
                profile = user_extra_reg.save(commit=False)
                profile.user = user
                print(profile)
                profile.save()
                data_dict['registered'] = True
                logging_username = temp_dict['username']
                logging_password = temp_dict['password']
                logged_user = authenticate(username=logging_username, password=logging_password)
                if logged_user:
                    login(request, logged_user)

    return render(request, 'user_content/register.html', data_dict)


def user_login(request):
    data_dict = {
        'login_failed': False,
        'account_not_active': False,
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                data_dict['login_failed'] = False
                data_dict['account_not_active'] = False
                return render(request, 'user_content/index.html', data_dict)
            else:
                data_dict['account_not_active'] = True
        else:
            data_dict['login_failed'] = True
    return render(request, 'user_content/login.html', data_dict)


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'main_app/index.html', {})


def index(request):
    data_dict = {}
    return render(request, 'user_content/index.html', data_dict)


def user_profile_view(request):
    username = request.user
    user_main_profile = models.User.objects.filter(username=username)
    user_id = user_main_profile.values_list('id')[0][0]
    user_extra_info = models.SiteUser.objects.filter(user_id=user_id)
    data_dict = {
        'main_info': user_main_profile,
        'extra_info': user_extra_info,
    }
    print(data_dict['extra_info'].values_list())
    return render(request, 'user_content/profile_view.html', data_dict)
