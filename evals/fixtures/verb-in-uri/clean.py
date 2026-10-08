import os

from django.urls import path

from . import views

urlpatterns = [
    path("orders/", views.index),
    path("orders/<int:pk>/", views.detail),
]

KEY = os.environ.get("CREATE_KEY")
VALUE = {"a": 1}.get("get_value")
