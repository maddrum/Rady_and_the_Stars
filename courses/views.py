from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models


# Create your views here.
class CoursesListView(ListView):
    model = models.Courses
    context_object_name = 'courses'
    template_name = 'courses/courses.html'

    # Пренадписване на резултата който дава ListView - за да покаже само логнатите юзъри
    def get_queryset(self):
        queryset = super(CoursesListView, self).get_queryset()
        queryset = queryset.filter(user_visited_course=self.request.user)
        return queryset


class CoursesUrlView(DetailView):
    template_name = 'courses/courses_links.html'
    model = models.Courses
    context_object_name = 'links'
