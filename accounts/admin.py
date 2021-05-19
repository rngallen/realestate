from django.contrib import admin
from .models import Profile

# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [
        "realtor",
        "first_name",
        "last_name",
        "email",
        "phone",
        "gender",
        "status",
        "registered",
    ]
    list_display_links = ["realtor", "first_name", "last_name"]
    search_fields = ["first_name", "last_name", "bio"]
    list_per_page = 11
