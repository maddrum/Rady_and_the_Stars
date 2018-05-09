from django.shortcuts import render, HttpResponse
from tarot_of_the_day import models
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.utils import timezone


@login_required
def card_pick(request):
    current_date = timezone.localdate()
    data_dict = {}
    user_id = request.user.id
    day_check = models.UserCard.objects.filter(date_used=current_date, username_id=user_id).values_list()
    if day_check.__len__() == 0:
        models.UserCard().random_card(logged_user_id=user_id)
    day_tarot = models.TarotCard.objects.select_related().filter(
        user_card__date_used=current_date, user_card__username_id=user_id)
    data_dict['day_tarot'] = day_tarot
    user_tarot = models.UserCard.objects.filter(date_used=current_date, username_id=user_id)
    data_dict['user_tarot'] = user_tarot
    if request.method == "POST":
        current_pk = user_tarot.values_list('id')[0][0]
        new_note_value = request.POST['value']
        models.UserCard().change_user_note(pk=current_pk, new_user_note=new_note_value)
        return HttpResponse(new_note_value)

    return render(request, 'tarot_of_the_day/day_card.html', data_dict)
