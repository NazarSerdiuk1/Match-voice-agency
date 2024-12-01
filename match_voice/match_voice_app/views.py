from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Tournament, Match, Commentator


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


def tournament_list(request):
    tournaments = Tournament.objects.all()
    paginate_by = 3

    paginator = Paginator(tournaments, paginate_by)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "tournaments" : tournaments,
        "page_obj": page_obj,
    }
    return render(request, "match_voice/tournament_list.html", context=context)
