from django.urls import re_path
from user_content import views

app_name = 'user_content'

urlpatterns = [
    re_path(r'register', views.user_register, name="register"),
    re_path(r'login', views.user_login, name="user_login"),
    re_path(r'logout', views.user_logout, name="logout"),
    re_path(r'index', views.index, name='index'),
    re_path(r'profile', views.user_profile_view, name='profile'),
    re_path(r'horoscope_list', views.UserHoroscopesListView.as_view(), name="horoscope_list"),
    re_path(r'^detail_text(?P<pk>\d+)', views.UserHoroscopesDetailView.as_view(), name="detail"),
    re_path(r'settings', views.ExtraUserSettingsUpdateView.as_view(), name='settings'),
    re_path(r'main_settings', views.MainUserSettingsUpdateView.as_view(), name='main_settings'),
]
