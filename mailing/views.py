import random

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseForbidden
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from blog.models import BlogArticle
from mailing.apps import MailingConfig
from mailing.forms import MailingSettingsForm, ServiceClientForm, MailingMessageForm
from mailing.models import MailingSettings, ServiceClient, MailingMessage, MailingClient

from django.shortcuts import render

app_name = MailingConfig.name


class ModelsListView(ListView):
    model = MailingSettings
    template_name = 'mailing/view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_mailings = MailingSettings.objects.all().count()
        filtered_mailings = MailingSettings.objects.filter(is_active=True).count()
        unique_clients = ServiceClient.objects.count()

        if BlogArticle.objects.exists():
            random_articles = random.sample(list(BlogArticle.objects.all()), 3)
        else:
            random_articles = []

        context.update({
            'all_mailings': all_mailings,
            'filtered_mailings': filtered_mailings,
            'unique_clients': unique_clients,
            'random_articles': random_articles,
        })

        return context


@method_decorator(login_required, name='dispatch')
class MailingListView(ListView):
    model = MailingSettings
    template_name = 'mailing_list.html'
    context = {
        'title': 'mailing list'
    }

    def get_queryset(self):
        return MailingSettings.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mailing List'
        return context


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    template_name = 'mailing/mailingsettings_form.html'
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
        if settings.CACHE_ENABLED:
            key = f"subject_list_{self.object.pk}"
            subject_list = cache.get(key)
            if subject_list is None:
                subject_list = ServiceClient.objects.all()
                cache.set(key, subject_list)
        else:
            subject_list = ServiceClient.objects.all()

        context_data['clients'] = subject_list
        context_data['mailing_pk'] = self.kwargs.get('pk')
        return context_data


def toggle_client(request, pk, client_pk):
    if MailingClient.objects.filter(client_id=client_pk, settings_id=pk).exists():
        MailingClient.objects.filter(client_id=client_pk, settings_id=pk).delete()
    else:
        MailingClient.objects.create(client_id=client_pk, settings_id=pk)
    return redirect(reverse('mailing:mailing_clients', args=[pk]))


class CustomMailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    success_url = reverse_lazy('mailing:mailing_list')
    login_url = '/users:login.html/'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.user != self.request.user:
            if self.raise_exception:
                raise PermissionDenied("You don't have access to this mailing.")
            else:
                return HttpResponseForbidden("You don't have access to this mailing.")
        return obj
