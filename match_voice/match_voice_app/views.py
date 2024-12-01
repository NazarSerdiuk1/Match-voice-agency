from django.shortcuts import render
from .models import Tournament,Match,Commentator


def index(request):
    context = {
        "title": "MatchVoice"
    }
    return render(request, "match_voice/index.html", context=context)


def search_view(request):
    query = request.GET.get("query", "")
    results = None

    if query:
        results = list(
            Tournament.objects.filter(name__icontains=query)
        ) + list(
            Commentator.objects.filter(
                username__icontains=query
            ) | Commentator.objects.filter(first_name__icontains=query) | Commentator.objects.filter(
                last_name__icontains=query)
        ) + list(
            Match.objects.filter(title__icontains=query)
        )

    return render(request, "match_voice/search.html", {"query": query, "results": results})
