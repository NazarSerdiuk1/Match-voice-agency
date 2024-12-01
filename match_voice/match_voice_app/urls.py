from django.urls import path

from .views import index, search_view, tournament_list

app_name = "match_voice"

urlpatterns = [
    path("", index, name="index"),
    path("search/", search_view, name="search"),
    path("tournaments/", tournament_list, name="tournament-list"),
]
