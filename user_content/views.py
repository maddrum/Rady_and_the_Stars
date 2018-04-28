from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.views.generic import DetailView, ListView
from . import models


# Create your views here.
def user_login(request):
    data_dict = {
        'login_failed': False,
        'account_not_active': False,
    }
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                data_dict['login_failed'] = False
                data_dict['account_not_active'] = False
                return render(request, 'user_content/index.html', data_dict)
            else:
                data_dict['account_not_active'] = True
        else:
            data_dict['login_failed'] = True
    return render(request, 'user_content/login.html', data_dict)


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'main_app/index.html', {})


def index(request):
    data_dict = {}
    return render(request, 'user_content/index.html', data_dict)


class CoursesListView(ListView):
    model = models.Courses
    context_object_name = 'courses'
    template_name = 'user_content/courses.html'
#Пренадписване на резултата който дава ListView - за да покаже само логнатите юзъри
    def get_queryset(self):
        queryset = super(CoursesListView, self).get_queryset()
        queryset = queryset.filter(user_visited_course=self.request.user)
        return queryset


class CoursesUrlView(DetailView):
    template_name = 'user_content/courses_links.html'
    model = models.Courses
    context_object_name = 'links'
