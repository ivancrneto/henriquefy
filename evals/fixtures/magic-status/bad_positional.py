from django.http import HttpResponse, JsonResponse
from fastapi import HTTPException
from flask import abort


def views(data, body):
    if not data:
        raise HTTPException(404, "missing")
    if body:
        return HttpResponse(body, 200)
    if data is None:
        abort(404)
    return JsonResponse({"count": 200}, 201)
