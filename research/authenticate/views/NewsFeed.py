from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from ..models import Feed
from ..service.FeedService import FeedService
from ..serializer.FeedSerializer import FeedSerializer

from library.response import response
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

feed_service = FeedService(Feed)


class FeedViewSet(viewsets.ModelViewSet):
    serializer_class = FeedSerializer

    permission_classes_by_action = {
        'list': [permissions.AllowAny],
        'create': [permissions.AllowAny],
        'retrieve': [permissions.AllowAny],
        'feed': [permissions.AllowAny]
    }

    def list(self, request, *args, **kwargs):
        """ GET, 목록조회

         TODO: 페이지네이션, 정렬키 적용

         """
        return Response(
            status=HTTP_200_OK,
            data=feed_service.read(query_param=request.query_params)
        )

    def create(self, request, *args, **kwargs):
        """ POST, 데이터 생성 """

        feed_serializer = FeedSerializer(data=request.data)
        if feed_serializer.is_valid(raise_exception=True):
            data = feed_service.create(
                valida_data=feed_serializer.validated_data,
                session=request.user
            )
        return response.Normal(data)

    def retrieve(self, request, *args, **kwargs):
        """ 상세목록조회 """
        query_result = feed_service.retrieve(path=kwargs)
        return response.Normal(data=query_result)

    @action(detail=True,
            methods=['get'],
            url_path="feed/(?P<user>[0-9]+)",
            )
    def feed(self, request, *args, **kwargs):
        """
        url path 변수를 두 개이상 사용할 때 본 action 데코레이터를 이용하자
        """
        print(kwargs)
        print("Nested Url Setup")
        return response.Normal()

    # 메소드별 권한 관리를 위해 오버라이딩 함
    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
