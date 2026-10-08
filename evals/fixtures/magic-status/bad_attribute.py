from django.http import HttpResponse


def missing(request):
    response = HttpResponse("gone")
    response.status_code = 404
    return response
