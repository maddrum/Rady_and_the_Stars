from django.shortcuts import render
from tarot_of_the_day import models
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.utils import timezone


@login_required
def card_pick(request):
    current_date = timezone.localdate()
    data_dict = {}
    user_id = request.user.id
    day_check = models.UserCard.objects.filter(date_used=current_date).values_list()
    if day_check.__len__() == 0:
        models.UserCard().random_card(logged_user_id=user_id)
    day_tarot = models.TarotCard.objects.select_related().filter(
        user_card__date_used=current_date, user_card__username_id=user_id)
    print(day_tarot)
    data_dict['day_tarot'] = day_tarot
    user_tarot = models.UserCard.objects.filter(date_used=current_date, username_id=user_id)
    data_dict['user_tarot'] = user_tarot
    return render(request, 'tarot_of_the_day/day_card.html', data_dict)


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['card_of_the_day'] = models.TarotCard.objects.filter(id=self.random_number)
    #     return context
