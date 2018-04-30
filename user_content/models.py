from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class SiteUser(models.Model):
    # Описва съдържанието на отделен юзър
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(blank=True, null=True)
    hour_of_birth = models.TimeField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)
    used_service = models.BooleanField(choices=((True, "Да"), (False, "Не")), default=False)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    city_of_birth = models.CharField(max_length=250, blank=True)
    country_of_birth = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_content:profile')


class TextsForUser(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    article_text = models.CharField(max_length=20000)

# class Courses(models.Model):
#     # описва отделните курсове - начало край и име
#     course_name = models.CharField(max_length=500, unique=True)
#     course_start_date = models.DateField()
#     course_end_date = models.DateField()
#     user_visited_course = models.ManyToManyField(User, related_name='user_visited')
#
#     def __str__(self):
#         return self.course_name
#
#
# class CoursesVideoLinks(models.Model):
#     # линковете на видеото от курса
#     courseID_video = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='course_video')
#     URL_link = models.URLField(blank=False)
#     video_is_about = models.CharField(max_length=150)
