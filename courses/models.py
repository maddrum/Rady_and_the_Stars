from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Courses(models.Model):
    # описва отделните курсове - начало край и име
    course_name = models.CharField(max_length=500, unique=True)
    course_start_date = models.DateField()
    course_end_date = models.DateField()
    user_visited_course = models.ManyToManyField(User, related_name='user_visited')

    def __str__(self):
        return self.course_name


class CoursesVideoLinks(models.Model):
    # линковете на видеото от курса
    courseID_video = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='course_video')
    URL_link = models.URLField(blank=False)
    video_is_about = models.CharField(max_length=150)
