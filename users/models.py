from django.db.models import CharField, TextChoices
from django.contrib.auth.models import AbstractUser


class UserTypeChoices(TextChoices):
    ADMIN = 'admin', 'Admin'
    OPERATOR = 'operator', 'Operator'
    REGULAR = 'regular', 'Regular'
    MODERATOR = 'moderator', 'Moderator'


class CustomUser(AbstractUser):
    user_type = CharField(
        max_length=12, 
        choices=UserTypeChoices.choices,
        default=UserTypeChoices.REGULAR
    )
    phone_number = CharField(max_length=20, default='111', blank=True, null=True)


# user = CustomUser.objects.filter(
#     user_type=UserTypeChoices.OPERATOR
# ).first()
