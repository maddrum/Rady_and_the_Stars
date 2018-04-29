from django.shortcuts import render
from main_app.forms import SiteContactsForm, SiteOrderForm


# Create your views here.

def index(request):
    data_dict = {}
    return render(request, 'main_app/index.html', data_dict)


def order(request):
    order_form = SiteOrderForm()
    data_dict = {
        'whole_form': order_form,
        'order_completed': False
    }
    if request.method == "POST":
        user_form = SiteOrderForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            data_dict['order_completed'] = True
    return render(request, 'main_app/order.html', data_dict)


def Rady(request):
    data_dict = {}
    return render(request, 'main_app/Rady.html', data_dict)


def contacts(request):
    contacts_form = SiteContactsForm()
    data_dict = {
        'message_received': False,
        'whole_form': contacts_form
    }
    if request.method == 'POST':
        contacts_form = SiteContactsForm(request.POST)
        if contacts_form.is_valid():
            data_dict['message_received'] = True
            contacts_form.save()
    print(data_dict)

    return render(request, 'main_app/contacts.html', data_dict)
