from django.db import models

from apps.authentication.models import User


class Artist(models.Model):
    nickname = models.CharField(max_length=30)
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        default=None,
    )

    def __str__(self):
        return self.nickname
