from django.contrib import admin
from . models import Category, House, Contact
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ["title", "realtor","is_published", "city", "posted",]
    list_display_links = ['realtor',"title" ]
    list_filter = ['realtor', "city"]
    list_editable = ["is_published",]
    search_fields = ["title","description","state","address","city","zipcode",]
    list_per_page = 13


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["id","title", "house_id","user_id", "name","email","phone","contact_date"]
    list_display_links = ["title","name"]
    search_fields = ["title", "name", "email","phone"]
    list_per_page = 10