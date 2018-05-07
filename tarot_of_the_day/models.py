from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


# Create your models here.

class TarotCard(models.Model):
    name = models.CharField(max_length=150, unique=True)
    picture_name = models.CharField(max_length=150, unique=True)
    meaning = models.TextField()


class UserCard(models.Model):
    user = get_user_model()
    username = models.ForeignKey(user, on_delete=models.CASCADE)
    date_used = models.DateField(default=timezone.now)
    date_card = models.ForeignKey(TarotCard, on_delete=models.CASCADE)
    user_notes = models.TextField(blank=True)

    def set_card_date(self):
        self.date_used = timezone.now()
        self.save()
