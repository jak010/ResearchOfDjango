import jwt


class MyAuthentication:
    def __init__(self, get_response):
        self.get_response = get_response
        # 최초 설정 및 초기화

    def __call__(self, request):
        # 뷰가 호출되기 전에 실행될 코드들
        from pprint import pprint
        response = self.get_response(request)
        print(" =" * 25)
        _jwt = request.META.get('HTTP_AUTHRIZATION')

        try:
            print(jwt.decode(_jwt, '1', algorithms='HS256'))
        except jwt.exceptions.DecodeError:
            print("be login")
            print(response)
            return response



        # 뷰가 호출된 뒤에 실행될 코드들


