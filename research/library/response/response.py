from django.http import HttpResponse
from django.http import JsonResponse

from rest_framework import status


class Normal(JsonResponse):
    def __init__(self, data=None):
        self.response = {
            'status': status.HTTP_200_OK,
            'code': 20000
        }

        if data is not None:
            self.response.update(data=data)

        super().__init__(
            data=self.response,
        )


class BadRequest(JsonResponse):
    def __init__(self):
        super().__init__(
            data={
                'status': status.HTTP_400_BAD_REQUEST,
                'code': 40000,
            },
        )
