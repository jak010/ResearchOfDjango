from ..models import Feed
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from ..models import User
from django.contrib.auth.models import AnonymousUser


class FeedService(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['title', 'content']

    @classmethod
    def read(cls):
        data = [
            {
                'id': item.id,
                'user_pk': item.user_id.pk,
                'title': item.title,
                'content': item.content,
                'create_at': item.create_at.strftime("%Y-%d-%m, %H:%M:%S"),
                'update_at': item.update_at.strftime("%Y-%d-%m, %H:%M:%S")

            } for item in Feed.objects.all()
        ]
        return data

    @staticmethod
    def retrieve(pk):

        data = [
            {
                'id': item.id,
                'user_pk': item.user_id.pk,
                'title': item.title,
                'content': item.content,
                'create_at': item.create_at.strftime("%Y-%d-%m, %H:%M:%S"),
                'update_at': item.update_at.strftime("%Y-%d-%m, %H:%M:%S")

            } for item in Feed.objects.filter(id=int(pk))
        ]

        return data

    def create(self):
        try:
            self.validated_data.update({'user_id': self.context.user})
        except AttributeError:
            self.validated_data.update({'user_id': User(email="anonymous@anon.com")})

        return Feed.objects.create(**self.validated_data)
