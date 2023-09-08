from django.urls import path

from mailing.views import MailingListView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsDeleteView, ServiceClientListView, ServiceClientCreateView, ServiceClientUpdateView, \
    ServiceClientDeleteView

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingSettingsCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>', MailingSettingsUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>', MailingSettingsDeleteView.as_view(), name='mailing_delete'),


    path('clients/', ServiceClientListView.as_view(), name='clients'),
    path('clients/create/', ServiceClientCreateView.as_view(), name='clients_create'),
    path('clients/update/<int:pk>/', ServiceClientUpdateView.as_view(), name='clients_update'),
    path('clients/delete/<int:pk>/', ServiceClientDeleteView.as_view(), name='clients_delete'),
]
