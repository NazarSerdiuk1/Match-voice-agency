from django.urls import path

from .views import index, search_view, TournamentListView, TournamentDetailView

app_name = "match_voice"

urlpatterns = [
    path("", index, name="index"),
    path("search/", search_view, name="search"),
    path("tournaments/", TournamentListView.as_view(), name="tournament-list"),
    path(
        "tournaments/<int:pk>/",
        TournamentDetailView.as_view(),
        name="tournament-detail",
    ),
]
