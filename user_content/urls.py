from django.conf.urls import url
from user_content import views

app_name = 'user_content'

urlpatterns = [
    url(r'register/', views.user_register, name="register"),
    url(r'login/', views.user_login, name="user_login"),
    url(r'logout/', views.user_logout, name="logout"),
    url(r'index/', views.index, name='index'),
    url(r'profile/', views.user_profile_view, name='profile'),
    url(r'horoscope_list/', views.UserHoroscopesListView.as_view(), name="horoscope_list"),
    url(r'detail_text(?P<pk>\d+)/', views.UserHoroscopesDetailView.as_view(), name="detail"),
    url(r'settings/', views.ExtraUserSettingsUpdateView.as_view(), name='settings'),
    url(r'main_settings/', views.MainUserSettingsUpdateView.as_view(), name='main_settings'),
]
