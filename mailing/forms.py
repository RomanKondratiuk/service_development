from django import forms
from mailing.models import MailingSettings, ServiceClient, MailingMessage


class MailingSettingsForm(forms.ModelForm):
    # class Meta:
    #     model = MailingSettings
    #     fields = '__all__'
    class Meta:
        model = MailingSettings
        fields = '__all__'  # ['time', 'period', 'status', 'is_active', 'message', 'client']
        widgets = {
            'clients': forms.CheckboxSelectMultiple(),
        }


class ServiceClientForm(forms.ModelForm):
    class Meta:
        model = ServiceClient
        fields = '__all__'


class MailingMessageForm(forms.ModelForm):
    class Meta:
        model = MailingMessage
        fields = '__all__'
