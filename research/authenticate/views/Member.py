from library.response import response

from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from ..service.UserService import UserService
from ..service.UserService import UserLoginService

# TEST
from django.http import HttpResponse


class MemberLoginView(TokenObtainPairView):
    serializer_class = UserLoginService


class Register(APIView):

    def post(self, request):
        """ 유저 등록하기 """
        service = UserService(data=request.data)

        if service.is_valid(raise_exception=True):
            service.register(validated_data=service.validated_data)

        return response.Normal()


class PublishToken(APIView):

    def post(self, request):
        service = UserService(data=request.data)

        # is_valid 는 db에 데이터가 들어있는지 체크해서
        # 있으면 True를
        # 없으면 False를 return 하는 듯
        print(service.user_chcker(service.initial_data))

        return HttpResponse()


class Member(APIView):

    def get(self, request):
        """ 유저 목록 조회하기 """

        user_service = UserService()

        if (users := user_service.get_users()) is not None:
            return response.Normal(data=users)
