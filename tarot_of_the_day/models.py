from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.utils import timezone
from random import randint


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

    def random_card(self, logged_user_id):
        current_date = timezone.localdate()
        default_note = 'Твоята бележка за ' + str(current_date)
        self.username_id = logged_user_id
        self.date_used = current_date
        self.user_notes = default_note
        random_number = randint(1, 78)
        self.date_card_id = random_number
        self.save()
