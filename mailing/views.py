from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mailing.apps import MailingConfig
from mailing.forms import MailingSettingsForm, ServiceClientForm
from mailing.models import MailingSettings, ServiceClient

app_name = MailingConfig.name


class MailingListView(ListView):
    model = MailingSettings
    context = {
        'title': 'mailing list'
    }


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailing_list')


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy('mailing:mailing_list')


class ServiceClientListView(ListView):
    model = ServiceClient
    context = {
        'title': 'clients list'
    }


class ServiceClientCreateView(CreateView):
    model = ServiceClient
    form_class = ServiceClientForm
    success_url = reverse_lazy('mailing:clients')


class ServiceClientUpdateView(UpdateView):
    model = ServiceClient
    form_class = ServiceClientForm
    success_url = reverse_lazy('mailing:clients')


class ServiceClientDeleteView(DeleteView):
    model = ServiceClient
    success_url = reverse_lazy('mailing:clients')
