from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='phone', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)

    email_verification_token = models.CharField(max_length=128, unique=True, **NULLABLE)

    def generate_email_verification_token(self):
        token = get_random_string(128)
        self.email_verification_token = token
        self.save()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []