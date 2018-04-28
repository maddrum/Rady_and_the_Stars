from django.shortcuts import render
from main_app.forms import UserRegisterForm
from main_app.forms import SiteContactsForm, SiteOrderForm
from django.contrib.auth import authenticate, login


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
        'whole_form': contacts_form,
    }
    if request.method == 'POST':
        contacts_form = SiteContactsForm(request.POST)
        if contacts_form.is_valid():
            contacts_form.save()
            data_dict['message_received']: True
    return render(request, 'main_app/contacts.html', data_dict)


def user_register(request):
    user_reg = UserRegisterForm()
    data_dict = {
        'register_form': user_reg,
        'registered': False,
        'passwords_not_match': False,
        'valid_data': True
    }
    if request.method == "POST":
        user_reg = UserRegisterForm(request.POST)
        if user_reg.is_valid():
            temp_dict = user_reg.data
            if temp_dict['password'] != temp_dict['repeat_password']:
                data_dict['registered'] = False
                data_dict['passwords_not_match'] = True
            else:
                user = user_reg.save()
                user.set_password(user.password)
                user.save()
                data_dict['registered'] = True
                logging_username = temp_dict['username']
                logging_password = temp_dict['password']
                logged_user = authenticate(username=logging_username, password=logging_password)
                if logged_user:
                    login(request, logged_user)
    return render(request, 'main_app/register.html', data_dict)
