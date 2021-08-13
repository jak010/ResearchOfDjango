import jwt
import datetime

from django.db import models
from config import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from .manager.UserManager import UserManager


# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def get_user_email(self):
        return self.email

    def get_user_token(self):
        token = jwt.encode(
            payload={
                'email': self.get_user_email(),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=200)
            },
            key=settings.SECRET_KEY,
            algorithm='HS256'
        )
        return token
