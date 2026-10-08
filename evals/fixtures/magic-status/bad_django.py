from django.http import JsonResponse


def create(request):
    data = {"id": 1}
    return JsonResponse(data, status=201)


class Created(JsonResponse):
    status_code = 201
