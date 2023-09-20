from django.db import models

NULLABLE = {'blank': True, 'null': True}


class ServiceClient(models.Model):
    email = models.EmailField(verbose_name='email')
    first_name = models.CharField(**NULLABLE, max_length=150, verbose_name='first_name')
    last_name = models.CharField(**NULLABLE, max_length=150, verbose_name='last_name')
    comment = models.TextField(**NULLABLE, verbose_name='comment')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    class Meta:
        verbose_name = 'client'
        verbose_name_plural = 'clients'


class MailingSettings(models.Model):

    PERIOD_DAILY = 'daily'
    PERIOD_WEEKLY = 'weekly'
    PERIOD_MONTHLY = 'monthly'

    PERIODS = (
        (PERIOD_DAILY, 'daily'),
        (PERIOD_WEEKLY, 'weekly'),
        (PERIOD_MONTHLY, 'monthly'),
    )

    STATUS_CREATED = 'created'
    STATUS_STARTED = 'started'
    STATUS_DONE = 'done'
    STATUSES = (
        (STATUS_STARTED, 'started'),
        (STATUS_CREATED, 'created'),
        (STATUS_DONE, 'done'),
    )

    time = models.TimeField(verbose_name='Time')
    period = models.CharField(max_length=20, choices=PERIODS, default=PERIOD_DAILY, verbose_name='period')
    status = models.CharField(max_length=20, choices=STATUSES, default=STATUS_CREATED, verbose_name='status')

    message = models.ForeignKey('MailingMessage', on_delete=models.CASCADE, verbose_name='message', **NULLABLE)

    def __str__(self):
        return f'{self.time} / {self.period}'

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'


class MailingClient(models.Model):
    client = models.ForeignKey(ServiceClient, on_delete=models.CASCADE, verbose_name='client')
    settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='setting')

    def __str__(self):
        return f'{self.client} / {self.settings}'

    class Meta:
        verbose_name = 'Newsletter client'
        verbose_name_plural = 'Newsletter clients'


class MailingMessage(models.Model):
    subject = models.CharField(max_length=250, verbose_name='Topic')
    message = models.TextField(verbose_name='Body')

    def __str__(self):
        return f'{self.subject}'

    class Meta:
        verbose_name = 'Letter'
        verbose_name_plural = 'Letters'


class MailingLog(models.Model):
    STATUS_OK = 'ok'
    STATUS_FAILED = 'failed'
    STATUSES = (
        (STATUS_OK, 'Successfully'),
        (STATUS_FAILED, 'Error'),
    )

    client = models.ForeignKey(ServiceClient, on_delete=models.CASCADE, verbose_name='client')
    settings = models.ForeignKey(MailingSettings, on_delete=models.CASCADE, verbose_name='setting')

    status = models.CharField(max_length=50, choices=STATUSES, default=STATUS_OK, verbose_name='status')

    date_last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='date last attempt')

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'


