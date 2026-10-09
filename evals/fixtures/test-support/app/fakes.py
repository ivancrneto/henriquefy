from unittest import mock

from django.http import HttpResponse


def failing_gateway():
    reply = HttpResponse(b"", 503)
    reply.status_code = 500
    return mock.Mock(send=mock.Mock(return_value=reply))
