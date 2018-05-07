from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.views.generic import DetailView, ListView, UpdateView, TemplateView, CreateView
from user_content.forms import UserCreateForm
from . import models
from django.urls import reverse_lazy


# Create your views here.
class UserRegister(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('user_content:index')
    template_name = 'user_content/register.html'


# def user_register(request):
#     user_reg = UserRegisterForm()
#     user_extra_reg = UserRegisterExtraDataForm()
#     data_dict = {
#         'register_form': user_reg,
#         'extra_data_form': user_extra_reg,
#         'registered': False,
#         'passwords_not_match': False,
#         'valid_data': True
#     }
#     if request.method == "POST":
#         user_reg = UserRegisterForm(request.POST)
#         user_extra_reg = UserRegisterExtraDataForm(request.POST)
#         if user_reg.is_valid() and user_extra_reg.is_valid():
#             temp_dict = user_reg.data
#             if temp_dict['password'] != temp_dict['repeat_password']:
#                 data_dict['registered'] = False
#                 data_dict['passwords_not_match'] = True
#             else:
#                 user = user_reg.save()
#                 user.set_password(user.password)
#                 user.save()
#                 print(user)
#                 profile = user_extra_reg.save(commit=False)
#                 profile.user = user
#                 print(profile)
#                 profile.save()
#                 data_dict['registered'] = True
#                 logging_username = temp_dict['username']
#                 logging_password = temp_dict['password']
#                 logged_user = authenticate(username=logging_username, password=logging_password)
#                 if logged_user:
#                     login(request, logged_user)
#
#     return render(request, 'user_content/register.html', data_dict)


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'user_content/index.html'


@login_required
def user_profile_view(request):
    username = request.user
    user_main_profile = models.User.objects.filter(username=username)
    try:
        user_id = user_main_profile.values_list('id')[0][0]
    except IndexError:
        return redirect('index')
    user_extra_info = models.SiteUser.objects.filter(user_id=user_id)
    data_dict = {
        'main_info': user_main_profile,
        'extra_info': user_extra_info,
    }

    return render(request, 'user_content/profile.html', data_dict)


class UserHoroscopesListView(LoginRequiredMixin, ListView):
    login_url = 'userportal/login/'
    model = models.TextsForUser
    context_object_name = 'horoscopes_list'
    template_name = "user_content/profile_horoscope_list_view.html"


    # def get_queryset(self):
    #     queryset = super(UserHoroscopesListView, self).get_queryset()
    #     username = self.request.user
    #     queryset = queryset.filter(username=username)
    #     return queryset


class UserHoroscopesDetailView(LoginRequiredMixin, DetailView):
    model = models.TextsForUser
    login_url = '/login'
    context_object_name = 'horoscopes_detail'
    template_name = 'user_content/profile_horoscope_detail_view.html'


class MainUserSettingsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'userportal/login/'
    model = models.User
    template_name = 'user_content/profile_main_settings_update.html'
    fields = ('email,first_name,last_name')


class ExtraUserSettingsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = 'userportal/login/'
    model = models.SiteUser
    template_name = 'user_content/profile_extra_settings_update.html'
    context_object_name = 'extra_info'
    fields = ('birthday', 'phone', 'city_of_birth')

    def get_object(self, queryset=None):
        username = self.request.user
        queryset = models.SiteUser.objects.get(user=username)
        return queryset

# def user_login(request):

# data_dict = {
#         'login_failed': False,
#         'account_not_active': False,
#     }
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 data_dict['login_failed'] = False
#                 data_dict['account_not_active'] = False
#                 return render(request, 'user_content/index.html', data_dict)
#             else:
#                 data_dict['account_not_active'] = True
#         else:
#             data_dict['login_failed'] = True
#     return render(request, 'user_content/login_old.html', data_dict)
#
#
# @login_required
# def user_logout(request):
#     logout(request)
#     return render(request, 'main_app/index.html', {})
