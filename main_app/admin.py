from django.contrib import admin
from main_app import models

# Register your models here.
admin.site.register(models.MenuItems)
admin.site.register(models.SiteContacts)
admin.site.register(models.SiteOrders)
