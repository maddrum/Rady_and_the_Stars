from django.conf.urls import url
from main_app import views

app_name = 'main_app'
urlpatterns = [
    url(r'contacts/$', views.Contacts.as_view(), name="contacts"),
    url('contacts/thank_you/$', views.ContactsThankYou.as_view(), name='contacts_thank_you'),
    url(r'order/$', views.Order.as_view(), name="order"),
    url('order/thank_you/$', views.OrderThankYou.as_view(), name='order_thank_you'),
    url(r'Rady/$', views.Rady.as_view(), name="Rady"),
]
