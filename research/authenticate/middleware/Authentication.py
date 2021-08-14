import jwt
from config import settings

from django.http import HttpResponseBadRequest

from pprint import pprint


class MyAuthentication:
    def __init__(self, get_response):
        self.get_response = get_response

        # 최초 설정 및 초기화

        # 허용할 URL 목록
        self.whitelist = [
            'authenticate/login'
        ]

    def __call__(self, request):
        # 뷰가 호출되기 전에 실행될 코드
        _jwt = request.META.get('HTTP_AUTHORIZATION')

        # jwt 토큰 검증
        if _jwt:
            try:
                jwt.decode(_jwt,
                           key=settings.SECRET_KEY,
                           algorithms='HS256')
            except jwt.exceptions.DecodeError:
                return HttpResponseBadRequest

        # 허용된 URL 인지 확인
        self.access_policy(request)

        # 뷰가 호출된 뒤에 실행될 코드들
        return self.get_response(request)

    def access_policy(self, req):
        if req.path not in self.whitelist:
            return HttpResponseBadRequest()
