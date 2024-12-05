from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    index,
    search_view,
    TournamentListView,
    TournamentDetailView,
    MatchListView,
    MatchDetailView,
    CommentatorListView,
    CommentatorDetailView,
    about,
    CustomLoginView,
    SignUpView,
)

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
    path("matches/", MatchListView.as_view(), name="match-list"),
    path("matches/<int:pk>/", MatchDetailView.as_view(), name="match-detail"),
    path("commentators/", CommentatorListView.as_view(), name="commentator-list"),
    path(
        "commentators/<int:pk>/",
        CommentatorDetailView.as_view(),
        name="commentator-detail",
    ),
    path("about/", about, name="about"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("signup/", SignUpView.as_view(), name="sign-up"),
    path(
        "logout/",
        LogoutView.as_view(next_page="/"),
        name="logout",
    ),
]
