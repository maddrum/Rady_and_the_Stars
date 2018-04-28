from django import template
from main_app.models import MenuItems

register = template.Library()


@register.simple_tag
def return_menu_items(logged_check):
    if logged_check == 'not_logged':
        menu_number = MenuItems.objects.filter(logged_in=False).values_list('menu_number')
    else:
        menu_number = MenuItems.objects.filter(logged_in=True).values_list('menu_number')
    data_dict = {}
    for item in menu_number:
        menu_item = MenuItems.objects.filter(menu_number=item[0]).values_list('menu_item')[0][0]
        menu_link = MenuItems.objects.filter(menu_number=item[0]).values_list('menu_link')[0][0]
        temp_arr = [menu_item, menu_link]
        data_dict[item[0]] = temp_arr
    return data_dict
