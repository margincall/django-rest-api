from django.db import models


class Artist(models.Model):
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return self.nickname
