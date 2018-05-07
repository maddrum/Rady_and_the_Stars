from django.shortcuts import render
from django.urls import reverse_lazy
from main_app.forms import SiteContactsForm, SiteOrderForm
from django.views.generic import TemplateView, CreateView


# Create your views here.

class Index(TemplateView):
    template_name = 'main_app/index.html'


class OrderThankYou(TemplateView):
    template_name = 'main_app/order_thank_you.html'


class ContactsThankYou(TemplateView):
    template_name = 'main_app/contacts_thank_you.html'


class Order(CreateView):
    form_class = SiteOrderForm
    template_name = 'main_app/order.html'
    success_url = reverse_lazy('main_app:order_thank_you')


class Rady(TemplateView):
    template_name = 'main_app/Rady.html'


class Contacts(CreateView):
    template_name = 'main_app/contacts.html'
    form_class = SiteContactsForm
    success_url = reverse_lazy('main_app:contacts_thank_you')
