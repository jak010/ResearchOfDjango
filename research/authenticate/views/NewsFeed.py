from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.views import APIView
from library.response import response
from ..service.FeedService import FeedService

from django.utils.decorators import method_decorator
from rest_framework import permissions


class FeedViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'list': [permissions.AllowAny]
    }

    def list(self, request, *args, **kwargs):

        return response.Normal(data=FeedService.read())

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]


class Feed(APIView):

    def get(self, request):
        return FeedService.read()

    def post(self, request):
        feed = FeedService(data=request.data, context=request)

        if feed.is_valid(raise_exception=True):
            feed.create()

        return response.Normal()
