from django.urls import path
from pages.models import Company, SocialNetwork
from .views import dashboard, detail, inquiry, listings, search

app_name = "estate"

urlpatterns = [
    path("", listings, name="listings"),
    path("dashboard", dashboard, name="dashboard"),
    path("detail/<int:pk>", detail, name="detail"),
    path("search", search, name="search"),
    path("iquiry", inquiry, name="inquiry"),
]
