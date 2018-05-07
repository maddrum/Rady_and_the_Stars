from django.contrib import admin
from tarot_of_the_day.models import TarotCard, UserCard

# Register your models here.
admin.site.register(UserCard)
admin.site.register(TarotCard)
