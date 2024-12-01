from django.shortcuts import render


def index(request):
    context = {
        "title": "MatchVoice"
    }
    return render(request, "match_voice/index.html", context=context)
