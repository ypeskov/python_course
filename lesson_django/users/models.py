from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    def __str__(self):
        return f'CustomUser(username={self.username}, email={self.email}, date_joined={self.date_joined})'
