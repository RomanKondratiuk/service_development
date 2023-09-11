from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from mailing.apps import MailingConfig
from mailing.forms import MailingSettingsForm, ServiceClientForm, MailingMessageForm
from mailing.models import MailingSettings, ServiceClient, MailingMessage, MailingClient

app_name = MailingConfig.name


class ModelsListView(ListView):
    model = MailingSettings
    template_name = 'mailing/view.html'


class MailingListView(ListView):
    model = MailingSettings
    context = {
        'title': 'mailing list'
    }
    # template_name = 'mailing/index.html'


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


class MailingMessageListView(ListView):
    model = MailingMessage
    context = {
        'title': 'message list'
    }


class MailingMessageCreateView(CreateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:messages')


class MailingMessageUpdateView(UpdateView):
    model = MailingMessage
    form_class = MailingMessageForm
    success_url = reverse_lazy('mailing:messages')


class MailingMessageDeleteView(DeleteView):
    model = MailingMessage
    success_url = reverse_lazy('mailing:messages')


class MailingClientsListView(ListView):
    model = MailingClient

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['clients'] = ServiceClient.objects.all()
        context_data['mailing_pk'] = self.kwargs.get('pk')
        return context_data


def toggle_client(request, pk, client_pk):
    if MailingClient.objects.filter(client_id=client_pk, settings_id=pk).exists():
        MailingClient.objects.filter(client_id=client_pk, settings_id=pk).delete()
    else:
        MailingClient.objects.create(client_id=client_pk, settings_id=pk)
    return redirect(reverse('mailing:mailing_clients', args=[pk]))
