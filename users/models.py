from django.db.models import CharField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = CharField(max_length=20, default='111', blank=True, null=True)
