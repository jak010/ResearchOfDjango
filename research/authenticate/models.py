from django.db import models

from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)


# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email, password):

        if not email:
            raise ValueError("Must Have User Email ")
        if not password:
            raise ValueError("Must Have User Password ")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        user.is_staff = False
        user.is_superuser = False
        return user

    def create_superuser(self, email, password):

        if not email:
            raise ValueError("Must Have User Email ")
        if not password:
            raise ValueError("Must Have User Password ")

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        user.is_staff = True
        user.is_superuser = True
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_user_email(self):
        return self.email
