from django.conf.urls import url
from main_app import views

app_name = 'main_app'
urlpatterns = [
    url(r'order/$', views.Order.as_view(), name="order"),
    url(r'Rady/$', views.Rady.as_view(), name="Rady"),
    url(r'contacts/$', views.Contacts.as_view(), name="contacts"),
    url('order/thank_you/$', views.OrderThankYou.as_view(), name='order_thank_you'),
    url('contacts/thank_you/$', views.ContactsThankYou.as_view(), name='contacts_thank_you'),
]
