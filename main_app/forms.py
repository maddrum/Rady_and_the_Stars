from django import forms
from django.forms import models
from main_app.models import SiteContacts, SiteOrders


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
