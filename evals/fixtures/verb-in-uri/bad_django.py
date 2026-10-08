from django.urls import path

from . import views

urlpatterns = [
    path("orders/create/", views.create),
    path("orders/<int:pk>/", views.detail),
]
