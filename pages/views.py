from django.shortcuts import render, redirect
from pages.models import Company, SocialNetwork
from estate.models import House
from django.contrib.auth.models import User
from estate.choices import bedroom_choices, state_choices, price_choices
# Create your views here.


def index(request):
    try:
        company = Company.objects.all()[:1].get()
        social = SocialNetwork.objects.all()[:1].get()
    except:
        company = []
        social = []
    houses = House.objects.filter(is_published=True, paid=False)[:3]
    context = {
        "company": company,
        "social": social,
        "houses": houses,
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices,
        "price_choices": price_choices,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    try:
        company = Company.objects.all()[:1].get()
        social = SocialNetwork.objects.all()[:1].get()
    except:
        company = []
        social = []
    realtors = User.objects.all()[:3]
    mvp = User.objects.filter(profile__is_mvp=True).first()
    context = {
        "company": company,
        "social": social,
        "realtors": realtors,
        "mvp": mvp,
    }
    return render(request, 'pages/about.html', context)
