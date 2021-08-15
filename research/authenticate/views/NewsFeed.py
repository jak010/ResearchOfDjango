from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from rest_framework.views import APIView
from library.response import response
from ..service.FeedService import FeedService

from django.utils.decorators import method_decorator
from rest_framework import permissions

from rest_framework.decorators import action

service = FeedService


class FeedViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'list': [permissions.AllowAny],
        'create': [permissions.AllowAny]
    }

    @action(methods=['get'], detail=False)
    def list(self, request, *args, **kwargs):
        return response.Normal(data=FeedService.read())

    @action(methods=['post'], detail=False)
    def create(self, request, *args, **kwargs):
        feed_service = service(data=request.data)
        if feed_service.is_valid(raise_exception=True):
            feed_service.create()
        return response.Normal()

    ## 메소드별 권한 관리를 위해 오버라이딩 함
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
