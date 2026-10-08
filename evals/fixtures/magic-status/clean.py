from http import HTTPStatus

from django.http import JsonResponse


def create(request):
    return JsonResponse({"id": 1}, status=HTTPStatus.CREATED)


class Created(JsonResponse):
    status_code = HTTPStatus.CREATED


TIMEOUT = 300
PORT = 8000
