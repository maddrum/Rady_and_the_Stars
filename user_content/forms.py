from django import forms
from django.forms import models
from user_content.models import SiteUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm


class SiteUserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': "Потребителско име:",
            'password1': "Парола:",
            'password2': "Моля, повторете паролата:",
            'email': 'Email',
        }


class UserRegisterExtraDataForm(models.ModelForm):
    class Meta:
        model = SiteUser
        fields = (
            'phone', 'used_service', 'birthday', 'hour_of_birth', 'city_of_birth',
            'country_of_birth')
        labels = {
            'used_service': 'Използвали ли сте мои услуги досега?',
            'birthday': 'Вашата рожденна дата',
            'hour_of_birth': 'Час на раждане',
            'city_of_birth': 'Град на раждане',
            'country_of_birth': 'Държава на раждане',
            'phone': 'Телефон'
        }


class UserMainDataForm(models.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name',)


