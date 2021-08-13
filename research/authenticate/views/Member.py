from library.response import response

from rest_framework.views import APIView

from ..service.UserService import UserService


# class MemberLoginView(TokenObtainPairView):
# DRF를 이용해 token 을 발급하는 방법
#     serializer_class = UserLoginService


class PublishToken(APIView):
    # 커스텀 유저 모델을 이용해 토큰을 발급하는 방법

    def post(self, request):
        """ jwt 토큰 발급하기 """
        service = UserService(data=request.data)

        user = service.validate()

        return response.Normal(data={
            'token': user.get_user_token().decode()
        })


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
