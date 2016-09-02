import re

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, is_admin=False):
        if not email:
            raise ValueError('Users must have an email address.')

        # email valid check
        if not re.match(r"^[_a-z0-9-]+(.[_a-z0-9-]+)*@(?:\w+\.)+\w+$", email):
            raise ValueError("not valid email error")

        email = self.normalize_email(email)

        user = self.model(email=email, is_admin=is_admin)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        return self.create_user(email, password, is_admin=True)


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        db_index=True,
    )
    nickname = models.CharField(max_length=30, default='')
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """"Does the user have a specific permission?"""
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        return True

    @property
    def is_staff(self):
        return self.is_admin
