from django.conf.urls import url
from user_content import views
from django.contrib.auth import views as login_view

app_name = 'user_content'

urlpatterns = [
    url(r'register/', views.UserRegister.as_view(), name="register"),
    url(r'index/', views.Index.as_view(), name='index'),
    url(r'profile/', views.user_profile_view, name='profile'),
    url(r'horoscope_list/', views.UserHoroscopesListView.as_view(), name="horoscope_list"),
    url(r'detail_text(?P<pk>\d+)/', views.UserHoroscopesDetailView.as_view(), name="detail"),
    url(r'settings/', views.ExtraUserSettingsUpdateView.as_view(), name='settings'),
    url(r'main_settings/', views.MainUserSettingsUpdateView.as_view(), name='main_settings'),
]
