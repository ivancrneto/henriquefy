from http import HTTPStatus


class CreatedView:
    status_code: int = 201


def accepted(resp):
    return resp.status_code in (200, HTTPStatus.ACCEPTED, 204)
