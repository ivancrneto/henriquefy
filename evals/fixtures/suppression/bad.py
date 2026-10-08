from django.http import JsonResponse


def create(request):
    return JsonResponse({}, status=201)  # henriquefy: ignore[api.magic-status]


def other(request):
    # henriquefy: ignore[api.magic-status, errors.bare-except]
    return JsonResponse({}, status=204)
