import json

from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder

from rest_framework import status

JSON_TYPE = "application/json"


def response_format(data, status, code):
    response_data = {
        'status': status,
        'code': code,
    }

    if data is None:
        response_data['data'] = list()
    else:
        response_data['data'] = data

    return json.dumps(obj=response_data, cls=DjangoJSONEncoder)


class Normal(HttpResponse):
    status_code = status.HTTP_200_OK

    def __init__(self, data=None):
        super(Normal, self).__init__(
            content=response_format(data=data, status=Normal.status_code, code=20000),
            content_type=JSON_TYPE
        )


class BadRequest(HttpResponse):
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, data=None):
        super(BadRequest, self).__init__(
            content=response_format(data=data, status=BadRequest.status_code, code=40001),
            content_type=JSON_TYPE
        )
