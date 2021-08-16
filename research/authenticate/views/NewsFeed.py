from rest_framework import viewsets
from library.response import response
from ..service.FeedService import FeedService

from rest_framework import permissions

from rest_framework.decorators import action

service = FeedService

from ..models import Feed


class FeedViewSet(viewsets.ModelViewSet):

    permission_classes_by_action = {
        'list': [permissions.AllowAny],
        'create': [permissions.AllowAny],
        'retrieve': [permissions.AllowAny],
        'feed': [permissions.AllowAny]
    }

    def list(self, request, *args, **kwargs):
        """ 목록조회 """
        return response.Normal(data=FeedService.read())

    def create(self, request, *args, **kwargs):
        """ 데이터 생성 """
        feed_service = service(data=request.data, context=request)
        if feed_service.is_valid(raise_exception=True):
            feed_service.create()
        return response.Normal()

    def retrieve(self, request, *args, **kwargs):
        """ 상세목록조회 """
        print(kwargs)
        return response.Normal(data=service.retrieve(kwargs['pk']))

    @action(detail=True,
            methods=['get'],
            url_path="feed/(?P<user>[0-9]+)",
            )
    def feed(self, request, *args, **kwargs):
        print(kwargs)
        print("Nested Url Setup")
        return response.Normal()

    ## 메소드별 권한 관리를 위해 오버라이딩 함
    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
