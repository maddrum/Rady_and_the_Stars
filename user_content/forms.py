from django import forms
from django.forms import models, widgets
from django.contrib.auth.models import User
from user_content.models import SiteUser, SiteOrders
from datetime import datetime


class UserRegisterForm(models.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput
        }
        help_texts = {
            'username': None,
        }
        labels = {
            'username': "Потребителско име:",
            'password': "Парола:",
            'email': 'Email',
        }

    repeat_password = forms.CharField(label="Моля, повторете паролата:", widget=widgets.PasswordInput)


class UserRegisterExtraInfoForm(models.ModelForm):
    class Meta:
        current_year = datetime.now().year
        model = SiteUser
        fields = ('profile_pic', 'phone', 'birthday', 'hour_of_birth',)
        widgets = {
            'birthday': widgets.DateTimeInput,  # формат - '%Y-%m-%d %H:%M'
        }
