from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
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
    return HttpResponse("This is the main page for challenges.")


"""
def january_challenge(request):
    return HttpResponse("This is the response for the january challenge.")


def february_challenge(request):
    return HttpResponse("This is the response for the february challenge.")
"""
# dynamic view


def monthly_challenge(request, month):
    parsing_string=render_to_string('challenges/challenge.html')
    return HttpResponse(parsing_string)
    #try:
        #challenge_text = monthly_challenges[month]
        #return HttpResponse(challenge_text)

    #except:
        #return HttpResponseNotFound("This month is not supported.")



def monthly_challenge_by_number(request, month):
    months=list(monthly_challenges.keys())
    redirect_month=months[month-1] # -1 cause indices start at 0
    return HttpResponseRedirect('/challenges/'+redirect_month)