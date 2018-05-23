from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import os
from django.db.models.signals import post_save


# Create your models here.
def path_and_rename(instance, filename):
    user_id = instance.user_id
    upload_to = 'profile_pics'
    filename = f'{user_id}_profile_pic.png'
    return os.path.join(upload_to, filename)


class SiteUser(models.Model):
    # Описва съдържанието на отделен юзър
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_data')
    birthday = models.DateField(blank=True, null=True)
    hour_of_birth = models.TimeField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True)
    used_service = models.BooleanField(choices=((True, "Да"), (False, "Не")), default=False)
    profile_pic = models.ImageField(upload_to=path_and_rename, blank=True)
    city_of_birth = models.CharField(max_length=250, blank=True)
    country_of_birth = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('user_content:profile')

    def null_writer(self, logged_user_id):
        self.user_id = logged_user_id
        self.save()

    def delete_profile_pic(self, logged_user_id):
        filename = f'{logged_user_id}_profile_pic.png'
        print(filename)
        current_dir = os.getcwd()
        media_folder = os.path.join(current_dir, 'media', 'profile_pics')
        os.chdir(media_folder)
        if os.path.exists(filename):
            print('check')
            os.remove(filename)
        os.chdir(current_dir)


class TextsForUser(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    article_text = models.CharField(max_length=20000)

#handle post save call if only new user is created. Links User and SiteUser tables.
def user_post_save_nullwriter_call(sender, instance, created, *args, **kwargs):
    print(created)
    if created:
        SiteUser().null_writer(instance.id)


post_save.connect(user_post_save_nullwriter_call, sender=User)
