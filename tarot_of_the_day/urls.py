from django.urls import re_path
from . import views

app_name = 'tarot_of_the_day'
urlpatterns = [
    # re_path(r'courses', views.CoursesListView.as_view(), name='courses_index'),
    # re_path(r'^(?P<pk>\d+)/$', views.CoursesUrlView.as_view(), name='links')
]
