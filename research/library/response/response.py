from rest_framework import status

from rest_framework.response import Response


class Http:
    type_json = "application/json"

    def Normal():
        return Response(
            {
                'status': status.HTTP_200_OK,
                'code': 20000
            },
            content_type=Http.type_json
        )

    def BadRequest():
        return Response(
            {
                'status': status.HTTP_400_BAD_REQUEST,
                'code': 40000,
            },
            content_type=Http.type_json
        )
