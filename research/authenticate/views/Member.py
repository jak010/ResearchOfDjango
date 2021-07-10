import json

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from ..service.UserService import UserService


class Register(APIView):

    def post(self, request):
        """ 유저 등록하기 """

        service = UserService(data=request.data)

        if service.is_valid():
            service.register(validated_data=service.validated_data)

        return HttpResponse(200)


class MemberInfo(APIView):

    def get(self, request):
        """ 현재 유저 정보 보여주기 """
        print(request.data)
        return HttpResponse(200)
