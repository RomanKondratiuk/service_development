from django.urls import path

from mailing.views import MailingListView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsDeleteView

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingSettingsCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>', MailingSettingsUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>', MailingSettingsDeleteView.as_view(), name='mailing_delete'),
]
