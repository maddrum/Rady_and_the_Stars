from django.urls import re_path
from user_content import views

app_name = 'user_content'

urlpatterns = [
    re_path(r'register', views.user_register, name="register"),
    re_path(r'login', views.user_login, name="user_login"),
    re_path(r'logout', views.user_logout, name="logout"),
    re_path(r'index', views.index, name='index'),
    re_path(r'courses', views.CoursesListView.as_view(), name='courses'),
    re_path(r'profile', views.user_profile_view, name='profile'),
    re_path(r'^test(?P<pk>\d+)/$',views.UserProfileView.as_view()),
    re_path(r'^(?P<pk>\d+)/$', views.CoursesUrlView.as_view(), name='links')
]
