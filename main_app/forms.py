from django import forms
from django.forms import models, widgets
from django.contrib.auth.models import User
from main_app.models import SiteContacts, SiteOrders


class UserRegisterForm(models.ModelForm):
    # регистрация на нов потребител. Потребителите ще се регистрират от мейн-апп, а после ще могат да попълват допълнителната информация в юзър конктент
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


class SiteContactsForm(models.ModelForm):
    class Meta:
        model = SiteContacts
        fields = ('names', 'email', 'phone', 'message')
        widgets = {
            'names': forms.TextInput(attrs={
                'placeholder': '*Моля въведете Вашите имена*',
            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Моля, въведете Вашият email',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '*Моля въведете Вашият телефон*',
            }),
            'message': forms.widgets.Textarea(attrs={
                'placeholder': '*Моля въведете Вашите въпрос*',
                'rows': "6",
            }),
        }


class SiteOrderForm(models.ModelForm):
    class Meta:
        model = SiteOrders
        fields = ('names', 'email', 'phone', 'service_requested', 'add_info')
        widgets = {
            'names': forms.TextInput(attrs={
                'placeholder': '*Моля въведете Вашите имена*',

            }),
            'email': forms.TextInput(attrs={
                'placeholder': 'Моля, въведете Вашият email',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '*Моля въведете Вашият телефон*',
            }),
            'add_info': forms.widgets.Textarea(attrs={
                'placeholder': 'Допълнителни указания',
                'rows': "6",
            }),

        }
