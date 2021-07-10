from library.response import response

from rest_framework.views import APIView

from ..service.UserService import UserService


class Register(APIView):

    def post(self, request):
        """ 유저 등록하기 """
        service = UserService(data=request.data)

        if not service.is_valid():
            return response.Http.BadRequest()

        service.register(validated_data=service.validated_data)

        return response.Http.Normal()
