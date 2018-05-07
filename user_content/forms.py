from django import forms
from django.forms import models
from user_content.models import SiteUser
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': "Потребителско име:",
            'password1': "Парола:",
            'password2': "Моля, повторете паролата:",
            'email': 'Email',
        }

    # class UserRegisterForm(models.ModelForm):
    #     # регистрация на нов потребител. Потребителите ще се регистрират от мейн-апп, а после ще могат да попълват допълнителната информация в юзър конктент
    #     class Meta:
    #         model = User
    #         fields = ('username', 'email', 'password')
    #         widgets = {
    #             'password': forms.PasswordInput,
    #             'email': widgets.EmailInput,
    #         }
    #         help_texts = {
    #             'username': None,
    #         }
    #         labels = {
    #             'username': "Потребителско име:",
    #             'password': "Парола:",
    #             'email': 'Email',
    #         }
    #
    #     repeat_password = forms.CharField(label="Моля, повторете паролата:", widget=widgets.PasswordInput)
    #

    class UserRegisterExtraDataForm(models.ModelForm):
        class Meta:
            model = SiteUser
            fields = (
                'profile_pic', 'phone', 'used_service', 'birthday', 'hour_of_birth', 'city_of_birth',
                'country_of_birth')
            labels = {
                'profile_pic': "Изберете профилна снимка",
                'used_service': 'Използвали ли сте мои услуги досега?',
                'birthday': 'Вашата рожденна дата',
                'hour_of_birth': 'Час на раждане',
                'city_of_birth': 'Град на раждане',
                'country_of_birth': 'Държава на раждане',
                'phone': 'Телефон'
            }
