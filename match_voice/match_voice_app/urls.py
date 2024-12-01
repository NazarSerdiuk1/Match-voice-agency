from django.urls import path

from .views import index, search_view

app_name = "match_voice"

urlpatterns = [
    path("", index, name="index"),
    path("search/", search_view, name="search"),

]
