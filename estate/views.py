from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from pages.models import Company, SocialNetwork
from .models import House, Contact
from .choices import price_choices, state_choices, bedroom_choices
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail


@login_required
def dashboard(request):
    """This method return realtor dashboard with his/her posted house listed"""
    try:
        company = Company.objects.all()[:1].get()
        social = SocialNetwork.objects.all()[:1].get()
    except:
        company = []
        social = []
    houses = House.objects.filter(realtor=request.user)
    context = {
        "company": company,
        "social": social,
        "houses": houses,
    }
    return render(request, 'estate/dashboard.html', context)


def detail(request, pk):
    """This method return details of the posted house"""
    try:
        company = Company.objects.all()[:1].get()
        social = SocialNetwork.objects.all()[:1].get()
    except:
        company = []
        social = []
    house = get_object_or_404(House, pk=pk)
    context = {
        "company": company,
        "social": social,
        "house": house,
    }
    return render(request, 'estate/detail.html', context)


def listings(request):
    """This method returns list of all houses from the database but with pagenation"""
    try:
        company = Company.objects.all()[:1].get()
        social = SocialNetwork.objects.all()[:1].get()
    except:
        company = []
        social = []
    houses = House.objects.filter(is_published=True, paid=False)
    paginator = Paginator(houses, 12)  # show 12 houses per page
    page_number = request.GET.get('page')
    house_list = paginator.get_page(page_number)
    context = {
        "company": company,
        "social": social,
        "houses": house_list,
    }
    return render(request, 'estate/listings.html', context)


def search(request):
    """This method return search results to user"""
    try:
        company = Company.objects.all()[:1].get()
        social = SocialNetwork.objects.all()[:1].get()
    except:
        company = []
        social = []
    search_results = House.objects.filter(is_published=True, paid=False)
    # keywords
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords:
            search_results = House.objects.filter(
                (Q(description__icontains=keywords) |
                 Q(address__icontains=keywords) |
                 Q(title__icontains=keywords)),
                is_published=True, paid=False)
    # city
    search_results = search_results
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            search_results = House.objects.filter(
                city__icontains=city, is_published=True, paid=False)
    # bedrooms
    search_results = search_results
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            search_results = House.objects.filter(
                bedroom__lte=bedrooms, is_published=True, paid=False)
    # price
    search_results = search_results
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            search_results = House.objects.filter(
                price__lte=price, is_published=True, paid=False)
        # keywords = request.GET.get('keywords')
        # city = request.GET.get('city')
        # state = request.GET.get('state')
        # bedrooms = request.GET.get('bedrooms')
        # price = request.GET.get('price')
        # search_results = House.objects.filter(
        #     Q(description__icontains=keywords) |
        #     Q(city__icontains=city) |
        #     Q(state__icontains=state) |
        #     Q(bedroom__gte=bedrooms) |
        #     Q(price__gte=price),
        #     is_published=True, paid=False
        # ).distinct()
    context = {
        "company": company,
        "social": social,
        "search_results": search_results,
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices,
        "values": request.GET,
    }
    return render(request, 'estate/search.html', context)


def inquiry(request):
    if request.method == "POST":
        title = request.POST["title"]
        house_id = request.POST["house_id"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        path = request.POST["path"]
        realtor_email = request.POST["realtor_email"]
        message = request.POST["message"]
        subject = f"Inquiry for {title} "
        from_email = email
        if request.user.is_authenticated:
            has_contacted = Contact.objects.filter(user_id=request.user.pk, house_id=house_id, email=email)
            if has_contacted:
                messages.error(request, "You have already make inquiry for this house.!!")
                return redirect(f"{path}")
            else:
                inquiry = Contact(title=title, house_id=house_id, name=name, email=email, phone=phone, message=message, user_id=request.user.pk)
                inquiry.save()
                messages.success(request, "Your Inquiry submitted successfully!")
                try:
                    send_mail(subject, message, from_email, [realtor_email, 'ramadhan@maycom.co.tz'])
                except BadHeaderError:
                    messages.error(request, f"Invalid Header Found, Kindly send again!!")
        else:
            inquiry = Contact(title=title, house_id=house_id, name=name, email=email, phone=phone, message=message, user_id=request.user.pk)
            inquiry.save()
            messages.success(request, "Your Inquiry submitted successfully!")
            try:
                send_mail(subject, message, from_email, [realtor_email, 'ramadhan@maycom.co.tz'])
            except BadHeaderError:
                messages.error(request, f"Invalid Header Found, Kindly send again!!")
    return redirect(f"{path}")
