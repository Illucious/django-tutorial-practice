from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}


def challenges_main(request):
    months=list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'month_list': months
    })


"""
def january_challenge(request):
    return HttpResponse("This is the response for the january challenge.")


def february_challenge(request):
    return HttpResponse("This is the response for the february challenge.")
"""
# dynamic view


def monthly_challenge(request, month):
    try:
        #month_name = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            'month_name': month,
            'text': monthly_challenges[month],
        })

    except:
        raise Http404()


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]  # -1 cause indices start at 0
    return HttpResponseRedirect('/challenges/'+redirect_month)
