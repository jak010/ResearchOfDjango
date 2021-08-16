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

    # DESC : AbstractBaseUser Model로 커스텀 jwt를 생성하려면 아래와 같이 21.08.16
    # def get_user_token(self):
    #     token = jwt.encode(
    #         payload={
    #             'email': self.get_user_email(),
    #             'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=15)
    #         },
    #         key=settings.SECRET_KEY,
    #         algorithm='HS256'
    #     )
    #     return token.decode()


class Feed(models.Model):
    id = models.BigAutoField(help_text='Feed ID', primary_key=True)
    user_id = models.IntegerField(help_text="User Id")
    title = models.TextField(help_text='Feed title', null=False)
    content = models.TextField(help_text='Feed Content', blank=True, null=True)

    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
