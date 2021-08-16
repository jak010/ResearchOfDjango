from ..models import Feed
from rest_framework import serializers
from ..models import User


class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = ['title', 'content']
