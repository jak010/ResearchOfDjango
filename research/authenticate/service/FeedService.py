from ..models import Feed
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault


class FeedService(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['title', 'content']

    @classmethod
    def read(cls):
        data = [
            {
                'user_pk': item.user_id.pk,
                'title': item.title,
                'content': item.content,
                'create_at': item.create_at.strftime("%Y-%d-%m, %H:%M:%S"),
                'update_at': item.update_at.strftime("%Y-%d-%m, %H:%M:%S")

            } for item in Feed.objects.all()
        ]
        return data

    def create(self):
        self.validated_data.update(
            {
                'user_id': self.context.user
            }
        )

        return Feed.objects.create(**self.validated_data)
