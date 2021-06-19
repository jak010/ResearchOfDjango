from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from ..serializer.MemberSerializer import AuthenticateSerializer


class Register(APIView):
    parser_classes = (JSONParser,)

    def __init__(self):
        super().__init__()

        self.serializer = AuthenticateSerializer

    def post(self, request, format=None):
        """ 유저 등록하기 """
        serializer = self.serializer(data=request.data)

        if serializer.is_valid():
            create_user = serializer.create_user(request.data)
            print(create_user)

        else:
            return HttpResponse(400)

        return HttpResponse(200)
