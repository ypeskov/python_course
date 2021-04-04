import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class EncPassword(models.Model):
    class Meta:
        verbose_name = 'encrypted password'
        verbose_name_plural = 'encrypted passwords'

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

    def get_absolute_url(self):
        return reverse('password_details', kwargs={'pk': self.pk})

    def __repr__(self):
        return f'EncPassword(name={self.name}, url={self.url}, username={self.username},\
         encrypted_password={self.encrypted_password}, password_user={self.password_user.id})'

    def __str__(self):
        return f'EncPassword(id={self.id}, name={self.name}, url={self.url}, username={self.username})'
