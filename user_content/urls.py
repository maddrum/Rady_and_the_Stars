from django.conf.urls import url, include
from user_content import views

app_name = 'user_content'

urlpatterns = [
    url(r'register/', views.UserRegister.as_view(), name="register"),
    url(r'index/', views.Index.as_view(), name='index'),
    url(r'profile/', views.user_profile_view, name='profile'),
    url(r'horoscope_list/', views.UserHoroscopesListView.as_view(), name="horoscope_list"),
    url(r'detail_text(?P<pk>\d+)/', views.UserHoroscopesDetailView.as_view(), name="detail"),
    url(r'settings/', views.ExtraUserSettingsUpdateView.as_view(), name='settings'),
    url(r'main_settings/', views.MainUserSettingsUpdateView.as_view(), name='main_settings'),
    url(r'courses/', include('courses.urls', namespace='user_courses')),
    url(r'tarot/', include('tarot_of_the_day.urls', namespace='user_tarot')),
    url(r'daily_tarot_list', views.UserTarotListView.as_view(), name='profile_tarot_list'),
    url(r'daily_tarot_detail(?P<pk>\d+)', views.UserTarotDetailView.as_view(), name='profile_tarot_detail'),
    url(r'daily_tarot_note_edit(?P<pk>\d+)', views.UserTarotNoteUpdateView.as_view(), name='profile__tarot_note_edit'),
]
