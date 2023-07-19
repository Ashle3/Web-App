from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("smallDogs/", views.smallDogs, name="smallDogs"),
    path("largeDogs/", views.largeDogs, name="largeDogs"),
]