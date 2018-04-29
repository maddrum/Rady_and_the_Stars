from django.urls import re_path
from main_app import views
from user_content import views as user_content_view

app_name = 'main_app'
urlpatterns = [
    re_path(r'^$', views.index, name="index"),
    re_path(r'index/', views.index),
    re_path(r'order/', views.order, name="order"),
    re_path(r'Rady/', views.Rady, name="Rady"),
    re_path(r'contacts/', views.contacts, name="contacts"),
    re_path(r'register', user_content_view.user_register)

]
