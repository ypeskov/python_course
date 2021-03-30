import uuid
from django.db import models
from django.contrib.auth import get_user_model


class EncPassword(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    name = models.CharField(max_length=100)
    url = models.URLField()
    username = models.CharField(max_length=200)
    encrypted_password = models.CharField(max_length=200)
    comment = models.TextField()

    password_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
