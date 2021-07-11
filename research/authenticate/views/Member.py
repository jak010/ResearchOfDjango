from library.response import response

from rest_framework.views import APIView
from ..service.UserService import UserService


class Register(APIView):

    def post(self, request):
        """ 유저 등록하기 """
        service = UserService(data=request.data)

        if service.is_valid(raise_exception=True):
            service.register(validated_data=service.validated_data)

        return response.Normal()


class Users(APIView):

    def get(self, request):
        pass