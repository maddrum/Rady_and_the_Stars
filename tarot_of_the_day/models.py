from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
from random import randint
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your models here.

class TarotCard(models.Model):
    name = models.CharField(max_length=150, unique=True)
    picture_name = models.CharField(max_length=50, unique=True)
    meaning = models.TextField()


class UserCard(models.Model):
    user = get_user_model()
    username = models.ForeignKey(user, on_delete=models.CASCADE)
    date_used = models.DateField(default='')
    date_card = models.ForeignKey(TarotCard, on_delete=models.CASCADE, related_name='user_card')
    user_notes = models.TextField(blank=True)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('user_site:profile_tarot_detail', kwargs={'pk': self.pk})

    def random_card(self, logged_user_id):
        current_date = timezone.localdate()
        default_note = 'Твоята бележка за ' + str(current_date)
        self.username_id = logged_user_id
        self.date_used = current_date
        self.user_notes = default_note
        random_number = randint(1, 78)
        self.date_card_id = random_number
        self.save()

    @classmethod
    def change_user_note(self, pk, new_user_note):
        filtered_info = self.objects.get(id=pk)
        filtered_info.user_notes = new_user_note
        filtered_info.save()
