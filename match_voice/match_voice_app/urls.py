from django.urls import path

from .views import index

app_name = "match_voice"

urlpatterns = [
    path("", index, name="index"),
]
