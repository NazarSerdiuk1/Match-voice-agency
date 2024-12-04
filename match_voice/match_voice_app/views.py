from django.shortcuts import render
from .models import Tournament, Match, Commentator
from django.views import generic
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from .forms import LoginForm, SignUpForm


def index(request):
    context = {"title": "MatchVoice"}
    return render(request, "match_voice/index.html", context=context)


def search_view(request):
    query = request.GET.get("query", "")
    results = None

    if query:
        results = (
            list(Tournament.objects.filter(name__icontains=query))
            + list(
                Commentator.objects.filter(username__icontains=query)
                | Commentator.objects.filter(first_name__icontains=query)
                | Commentator.objects.filter(last_name__icontains=query)
            )
            + list(Match.objects.filter(title__icontains=query))
        )

    return render(
        request, "match_voice/search.html", {"query": query, "results": results}
    )


class TournamentListView(generic.ListView):
    model = Tournament
    template_name = "match_voice/tournament_list.html"
    context_object_name = "tournaments"
    paginate_by = 3


class TournamentDetailView(generic.DetailView):
    model = Tournament
    template_name = "match_voice/tournament_detail.html"
    context_object_name = "tournament"


class MatchListView(generic.ListView):
    model = Match
    template_name = "match_voice/match_list.html"
    context_object_name = "matches"
    paginate_by = 3

    def get_queryset(self):
        return (
            Match.objects.select_related("tournament")
            .prefetch_related("commentators")
            .all()
        )


class MatchDetailView(generic.DetailView):
    model = Match
    template_name = "match_voice/match_detail.html"
    context_object_name = "match"


class CommentatorListView(generic.ListView):
    model = Commentator
    template_name = "match_voice/commentator_list.html"
    context_object_name = "commentators"
    paginate_by = 3


class CommentatorDetailView(generic.DetailView):
    model = Commentator
    template_name = "match_voice/commentator_detail.html"
    context_object_name = "commentator"


def about(request):
    return render(request, "match_voice/about.html")


class CustomLoginView(LoginView):
    template_name = "match_voice/login.html"
    form_class = LoginForm


class SignUpView(FormView):
    template_name = "match_voice/sign_up.html"
    form_class = SignUpForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

