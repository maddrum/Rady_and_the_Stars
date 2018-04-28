from django.urls import re_path
from main_app import views

app_name = 'main_app'
urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'index/', views.index),
    re_path(r'order/', views.order, name="order"),
    re_path(r'Rady/', views.Rady, name="Rady"),
    re_path(r'contacts/', views.contacts, name="contacts"),
    re_path(r'register', views.user_register, name="register"),

]
