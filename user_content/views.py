from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView, TemplateView, CreateView
from user_content.forms import SiteUserCreateForm
from user_content import models
from tarot_of_the_day import models as tarot_model
from django.urls import reverse_lazy


# Create your views here.
class UserRegister(CreateView):
    form_class = SiteUserCreateForm
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
    return render(request, 'user_content/profile_home.html', data_dict)


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
    login_url = 'userportal/login/'
    context_object_name = 'horoscopes_detail'
    template_name = 'user_content/profile_horoscope_detail_view.html'


class UserTarotListView(LoginRequiredMixin, ListView):
    model = tarot_model.UserCard
    context_object_name = 'tarot_list'
    template_name = 'user_content/profile_tarot_list.html'

    def get_queryset(self):
        queryset = super(UserTarotListView, self).get_queryset()
        user_id = self.request.user.id
        queryset = queryset.filter(username_id=user_id).order_by('-date_used')
        return queryset


class UserTarotDetailView(LoginRequiredMixin, DetailView):
    model = tarot_model.UserCard
    login_url = 'userportal/login/'
    context_object_name = 'tarot_detail'
    template_name = 'user_content/profile_tarot_detail.html'


class UserTarotNoteUpdateView(LoginRequiredMixin, UpdateView):
    model = tarot_model.UserCard
    login_url = 'userportal/login/'
    context_object_name = 'note_edit'
    template_name = 'user_content/profile_tarot_note_edit.html'
    fields = ('user_notes',)


class UserSettingsListView(LoginRequiredMixin, ListView):
    model = models.SiteUser
    context_object_name = 'settings_list'
    template_name = 'user_content/profile_settings_list_view.html'

    def get_queryset(self):
        queryset = super(UserSettingsListView, self).get_queryset()
        user_id = self.request.user.id
        queryset = queryset.filter(user_id=user_id)
        return queryset
