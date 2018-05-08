from django.conf.urls import url
from tarot_of_the_day import views

app_name = 'tarot_of_the_day'

urlpatterns = [
    url(r'^$', views.card_pick, name='card_of_the_day')
]
