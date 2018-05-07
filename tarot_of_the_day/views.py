from django.shortcuts import render
from tarot_of_the_day import models
from django.views.generic import TemplateView
from random import randint


# Create your views here.
class CardPick(TemplateView):
    model = models.TarotCard
    template_name = 'tarot_of_the_day/day_card.html'
    random_number = randint(1, 78)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['card_of_the_day'] = models.TarotCard.objects.filter(id=self.random_number)
        print(self.random_number)
        return context
