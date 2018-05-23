from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from user_content.forms import SiteUserCreateForm, UserUploadPic
from user_content import models
from tarot_of_the_day import models as tarot_model
from django.urls import reverse_lazy
from user_content.forms import UserRegisterExtraDataForm, UserMainDataForm
from django.contrib.auth import get_user_model


# Create your views here.
class UserRegister(CreateView):
    form_class = SiteUserCreateForm
    success_url = reverse_lazy('user_content:index')
    template_name = 'user_content/register.html'


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'user_content/index.html'


# @login_required
# def Index(request):
#     username = request.user
#     user_id = username.id
#     user_extra_info = models.SiteUser.objects.filter(user_id=user_id)
#     if not user_extra_info:
#         models.SiteUser().null_writer(logged_user_id=user_id)
#     return render(request, 'user_content/index.html')


@login_required
def user_profile_view(request):
    username = request.user
    user_main_profile = models.User.objects.filter(username=username)
    user_id = username.id
    user_extra_info = models.SiteUser.objects.filter(user_id=user_id)
    # if not user_extra_info:
    #     models.SiteUser().null_writer(logged_user_id=user_id)
    data_dict = {
        'main_info': user_main_profile,
        'extra_info': user_extra_info,
    }
    return render(request, 'user_content/profile_home.html', data_dict)


class UserHoroscopesListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
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
    login_url = '/login/'
    context_object_name = 'horoscopes_detail'
    template_name = 'user_content/profile_horoscope_detail_view.html'


class UserTarotListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
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
    login_url = '/login/'
    context_object_name = 'tarot_detail'
    template_name = 'user_content/profile_tarot_detail.html'


class UserTarotNoteUpdateView(LoginRequiredMixin, UpdateView):
    model = tarot_model.UserCard
    login_url = '/login/'
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


class UserExtraSettingsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = models.SiteUser
    form_class = UserRegisterExtraDataForm
    context_object_name = 'user_settings'
    template_name = 'user_content/profile_settings_update_view.html'
    success_url = '/userportal/settings/'

    def get_object(self, queryset=None):
        username_id = self.request.user.id
        queryset = models.SiteUser.objects.get(user_id=username_id)
        return queryset


class UserMainSettingsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = get_user_model()
    form_class = UserMainDataForm
    context_object_name = 'user_settings'
    template_name = 'user_content/profile_settings_update_view.html'
    success_url = '/userportal/settings/'

    def get_object(self, queryset=None):
        username_id = self.request.user.id
        queryset = self.model.objects.get(id=username_id)
        return queryset


@login_required
def profile_pic_upload(request):
    user_id = request.user.id
    print(user_id)
    content_dict = {}

    # TODO CRITERIAS FOR UPLOAD!
    # content_dict['criteria'] = False

    file_form = UserUploadPic()
    content_dict['form'] = file_form
    if request.method == "POST":
        file_form = UserUploadPic(request.POST)
        if file_form.is_valid():
            if 'profile_pic' in request.FILES:
                models.SiteUser().delete_profile_pic(logged_user_id=user_id)
                uploaded_pic = request.FILES['profile_pic']
                extra_profile_info = models.SiteUser.objects.get(user_id=user_id)
                extra_profile_info.profile_pic = uploaded_pic
                extra_profile_info.save()
        return redirect('user_site:profile')
    return render(request, 'user_content/profile_profile_picture.html', content_dict)
