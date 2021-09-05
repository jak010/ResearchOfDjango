from ..models import Feed

from rest_framework import serializers


class FeedSerializer(serializers.ModelSerializer):
    """ 선택적 """

    class Meta:
        model = Feed
        fields = ['title', 'content']


class FeedListSerializer(serializers.ModelSerializer):
    """ 목록조회 """

    class Meta:
        model = Feed
        fields = '__all__'
