from django.http import JsonResponse

from app.fakes import failing_gateway


def created_reply():
    return JsonResponse({"id": 1}, 201), failing_gateway()
