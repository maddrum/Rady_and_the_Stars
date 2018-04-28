from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MenuItems(models.Model):
    menu_number = models.IntegerField(primary_key=True, unique=True)
    menu_item = models.CharField(max_length=50)
    menu_link = models.CharField(max_length=200)
    # # За промяната на менюто за логнати потребители. True е ако има логнат потребител.
    logged_in = models.BooleanField()


class SiteContacts(models.Model):
    names = models.CharField(max_length=300, blank=False)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=False)
    message = models.CharField(max_length=1000, blank=False)
    message_replied = models.BooleanField(default=False)


class SiteOrders(models.Model):
    order_select = (('пълен', 'Пълен астрологичен пакет'), ('единичен', 'Хороскоп на един човек и прогноза'),
                    ('по тема', 'Разглеждане на една тема в хороскопа и прогноза'),
                    ('таро', 'Отговор на до 4 въпроса с таро'))
    names = models.CharField(max_length=300, blank=False)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.CharField(max_length=50, blank=False)
    service_requested = models.CharField(choices=order_select, blank=False, max_length=300)
    add_info = models.CharField(max_length=1000, blank=True)
    request_finished = models.BooleanField(default=False)
