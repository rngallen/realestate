from django.contrib import admin
from .models import Company, SocialNetwork

# Register your models here.


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]


@admin.register(SocialNetwork)
class SocialNetworkAdmin(admin.ModelAdmin):
    readonly_fields = [
        "company",
    ]
    list_display = [
        "company",
        "twitter",
        "facebook",
        "instagram",
    ]
