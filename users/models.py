from django.contrib.auth.models import AbstractUser
from django.db import models

from mailing.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')

    phone = models.CharField(max_length=35, verbose_name='phone', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='avatar', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []