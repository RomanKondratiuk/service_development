from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='skay.user.11@icloud.com',
            first_name='Admin',
            last_name='SkyPro',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('Aa010203')
        user.save()