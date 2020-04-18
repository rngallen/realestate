from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.utils.timezone import now
from datetime import date
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(_("Category Name"), max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CTGRY'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


def upload_path(instance, filename):
    today = date.today()
    today_path = today.strftime("%Y/%m")
    return f"{instance.realtor.pk}/estate/{today_path}/{instance.pk}/{filename}"


class House(models.Model):
    CURRENCY = [
        ("USD", "USD"),
        ("TZS", "TZS"),
    ]
    realtor = models.ForeignKey(User, verbose_name=_(
        "Realtor"), related_name="poster", on_delete=models.DO_NOTHING)
    title = models.CharField(_("Title"), max_length=60, db_column="TITLE")
    category = models.ForeignKey("estate.Category", verbose_name=_(
        "Category"), on_delete=models.CASCADE)
    address = models.CharField(
        _("Address"), max_length=60, blank=True, null=True, db_column="ADDRESS")
    city = models.CharField(_("City"), max_length=60,
                            blank=True, null=True, db_column="CITY")
    state = models.CharField(_("State"), max_length=60,
                             blank=True, null=True, db_column="STATE")
    zipcode = models.CharField(
        _("Zip Code"), max_length=20, blank=True, null=True, db_column="ZIP")
    description = models.TextField(_("Description"), blank=True, null=True)
    currency = models.CharField(_("Currency"), max_length=3, choices=CURRENCY)
    price = models.PositiveIntegerField(_("Price"), default=0)
    bedroom = models.PositiveIntegerField(_("Bedrooms"), default=1,)
    bathroom = models.PositiveIntegerField(_("Bathroom"), default=0)
    garage = models.PositiveIntegerField(_("Garage"), default=0)
    square_feet = models.PositiveIntegerField(
        _("Square Feet"), blank=True, null=True, )
    lot_size = models.DecimalField(
        _("Lot Size"), blank=True, null=True, max_digits=5, decimal_places=2)

    paid = models.BooleanField(_("Paid"), default=False)
    update = models.DateTimeField(
        _("Updated"), auto_now=True, auto_now_add=False)
    property_type = models.CharField(_("Propery Type"), max_length=50, )
    furnished = models.BooleanField(_("Furnished"), default=False)
    exchange_posibility = models.BooleanField(
        _("Exchange Possibilty"), default=False)
    realtor_fee = models.BooleanField(_("Realtor Fee"), default=True)

    image1 = models.ImageField(_("Main Image"), upload_to=upload_path)
    image2 = models.ImageField(
        _("Image"), upload_to=upload_path, blank=True, null=True)
    image3 = models.ImageField(
        _("Image"), upload_to=upload_path, blank=True, null=True)
    image4 = models.ImageField(
        _("Image"), upload_to=upload_path, blank=True, null=True)
    image5 = models.ImageField(
        _("Image"), upload_to=upload_path, blank=True, null=True)
    image6 = models.ImageField(
        _("Image"), upload_to=upload_path, blank=True, null=True)
    image7 = models.ImageField(
        _("Image"), upload_to=upload_path, blank=True, null=True)
    is_published = models.BooleanField(_("Is Published"), default=True)
    posted = models.DateTimeField(
        _("Posted"), auto_now=False, auto_now_add=True)
    available_date = models.DateField(_("Available"), default=now)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'HOUSE'
        managed = True
        verbose_name = 'House'
        verbose_name_plural = 'Houses'
        ordering = ['-pk', '-posted']

    def get_absolute_url(self):
        return reverse("estate:detail", kwargs={"pk": self.pk})


class Contact(models.Model):
    title = models.CharField(_("Title"), max_length=300)
    house_id = models.PositiveIntegerField(_("House Id"))
    name = models.CharField(_("Title"), max_length=200)
    email = models.EmailField(_("Email"), max_length=254)
    phone = models.CharField(_("Phone Number"), max_length=20)
    message = models.TextField(_("Message"), blank=True, null=True)
    contact_date = models.DateTimeField(
        _("Contact Date"), auto_now=False, auto_now_add=True)
    user_id = models.PositiveIntegerField(_("User Id"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'CONTACTS'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


'''
https://stackoverflow.com/questions/49827112/how-to-upload-multiple-images-from-a-single-choose-files-selector-in-django-ad
'''
