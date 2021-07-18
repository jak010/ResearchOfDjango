from library.response import response

from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from ..service.UserService import UserService
from ..service.UserService import UserLoginService


class MemberLoginView(TokenObtainPairView):
    serializer_class = UserLoginService


class Register(APIView):

    def post(self, request):
        """ 유저 등록하기 """
        service = UserService(data=request.data)

        if service.is_valid(raise_exception=True):
            service.register(validated_data=service.validated_data)

        return response.Normal()


class Member(APIView):

    def get(self, request):
        """ 유저 목록 조회하기 """

        user_service = UserService()

        if (users := user_service.get_users()) is not None:
            return response.Normal(data=users)
