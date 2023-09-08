from django import forms

from mailing.models import MailingSettings, ServiceClient


class MailingSettingsForm(forms.ModelForm):
    class Meta:
        model = MailingSettings
        fields = '__all__'


class ServiceClientForm(forms.ModelForm):
    class Meta:
        model = ServiceClient
        fields = '__all__'
