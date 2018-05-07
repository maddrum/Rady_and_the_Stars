from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView, TemplateView, CreateView
from user_content.forms import UserCreateForm
from . import models
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model


# Create your views here.
class UserRegister(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('user_content:index')
    template_name = 'user_content/register.html'


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

    def get_queryset(self):
        queryset = super(UserHoroscopesListView, self).get_queryset()
        username = self.request.user
        queryset = queryset.filter(username=username)
        return queryset


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
