from django.urls import path

from mailing import views
from mailing.views import MailingListView, MailingSettingsCreateView, MailingSettingsUpdateView, \
    MailingSettingsDeleteView, ServiceClientListView, ServiceClientCreateView, ServiceClientUpdateView, \
    ServiceClientDeleteView, MailingMessageListView, MailingMessageCreateView, MailingMessageUpdateView, \
    MailingMessageDeleteView, MailingClientsListView, ModelsListView, toggle_client

urlpatterns = [

    path('', ModelsListView.as_view(), name='base'),

    path('mailings', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingSettingsCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>', MailingSettingsUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>', MailingSettingsDeleteView.as_view(), name='mailing_delete'),


    path('clients/', ServiceClientListView.as_view(), name='clients'),
    path('clients/create/', ServiceClientCreateView.as_view(), name='clients_create'),
    path('clients/update/<int:pk>/', ServiceClientUpdateView.as_view(), name='clients_update'),
    path('clients/delete/<int:pk>/', ServiceClientDeleteView.as_view(), name='clients_delete'),

    path('messages/', MailingMessageListView.as_view(), name='messages'),
    path('messages/create/', MailingMessageCreateView.as_view(), name='messages_create'),
    path('messages/update/<int:pk>/', MailingMessageUpdateView.as_view(), name='messages_update'),
    path('messages/delete/<int:pk>/', MailingMessageDeleteView.as_view(), name='messages_delete'),

    # path('articles/', views.blog_articles, name='blog_articles'),
    #
    # path('<int:pk>/clients/', MailingClientsListView.as_view(), name='mailing_clients'),
    # path('<int:pk>/clients/add/<int:client_pk>/', toggle_client, name='mailing_clients_toggle'),
]
