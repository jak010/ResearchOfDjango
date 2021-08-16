from ..models import Feed
from rest_framework import serializers
from ..models import User


class FeedService(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['title', 'content']

    @classmethod
    def read(cls):
        query_result = Feed.objects.all()

        data = [
            {
                'id': query.id,
                'user_id': query.user_id,
                'title': query.title,
                'content': query.content,
                'create_at': query.create_at.strftime("%Y-%d-%m, %H:%M:%S"),
                'update_at': query.update_at.strftime("%Y-%d-%m, %H:%M:%S")

            } for query in query_result
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
            self.validated_data.update({'user_id': self.context.user.id})
        except AttributeError:
            self.validated_data.update({'user_id': 0})
        return Feed.objects.create(**self.validated_data)
