# Generated by Django 4.2.5 on 2023-09-21 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_alter_mailinglog_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailingsettings',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='is_active'),
        ),
    ]