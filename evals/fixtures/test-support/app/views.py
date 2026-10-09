from django.http import JsonResponse


def create(request):
    return JsonResponse({"id": 1}, 201)
