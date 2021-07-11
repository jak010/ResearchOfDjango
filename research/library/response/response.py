from django.http import JsonResponse

from rest_framework import status


class Normal(JsonResponse):
    def __init__(self):
        super().__init__(
            data={
                'status': status.HTTP_200_OK,
                'code': 20000,

            },
        )


class BadRequest(JsonResponse):
    def __init__(self):
        super().__init__(
            data={
                'status': status.HTTP_400_BAD_REQUEST,
                'code': 40000,
            },
        )
