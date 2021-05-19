from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Company(models.Model):
    name = models.CharField(
        _("Company Name"), max_length=180, blank=True, null=True, db_column="NAME"
    )
    tin_no = models.CharField(
        _("Tin Number"), max_length=20, blank=True, null=True, db_column="TIN"
    )
    vrn_no = models.CharField(
        _("VRN Number"), max_length=20, blank=True, null=True, db_column="VRN"
    )
    bus_reg_no = models.CharField(
        _("Company's Registration Number"),
        max_length=50,
        blank=True,
        null=True,
        db_column="REGNO",
    )
    address1 = models.CharField(
        _("Address"), max_length=60, blank=True, null=True, db_column="ADDRS1"
    )
    address2 = models.CharField(
        _("Address"), max_length=60, blank=True, null=True, db_column="ADDRS2"
    )
    address3 = models.CharField(
        _("Address"), max_length=60, blank=True, null=True, db_column="ADDRS3"
    )
    address4 = models.CharField(
        _("Address"), max_length=60, blank=True, null=True, db_column="ADDRS4"
    )
    city = models.CharField(
        _("City"), max_length=60, blank=True, null=True, db_column="CITY"
    )
    state = models.CharField(
        _("State"), max_length=60, blank=True, null=True, db_column="STATE"
    )
    zip_code = models.CharField(
        _("Zip Code"), max_length=60, blank=True, null=True, db_column="ZIP"
    )
    country = models.CharField(
        _("Country"), max_length=60, blank=True, null=True, db_column="COUNTRY"
    )
    phone = models.CharField(
        _("Telephone Number"), max_length=20, blank=True, null=True, db_column="PHONE"
    )
    fax = models.CharField(
        _("FaX"), max_length=20, blank=True, null=True, db_column="FAX"
    )
    email = models.EmailField(
        _("Email"), max_length=254, blank=True, null=True, db_column="EMAIL"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "COMPANY"
        managed = True
        verbose_name = "Company Profile"
        verbose_name_plural = "Company Profile"


class SocialNetwork(models.Model):
    company = models.OneToOneField(
        "pages.Company",
        verbose_name=_("Company"),
        related_name="social",
        on_delete=models.CASCADE,
        db_column="COMPANY",
    )
    twitter = models.URLField(
        _("Twitter"), max_length=200, blank=True, null=True, db_column="TWITTER"
    )
    facebook = models.URLField(
        _("Facebook"), max_length=200, blank=True, null=True, db_column="FB"
    )
    linkedin = models.URLField(
        _("LinkedIn"), max_length=200, blank=True, null=True, db_column="LKN"
    )
    instagram = models.URLField(
        _("Instgram"), max_length=200, blank=True, null=True, db_column="INSTA"
    )
    pinterest = models.URLField(
        _("Pinterest"), max_length=200, blank=True, null=True, db_column="PINT"
    )

    def __str__(self):
        return str(self.company)

    class Meta:
        db_table = "SNETWORK"
        managed = True
        verbose_name = "SocialNetwork"
        verbose_name_plural = "SocialNetworks"


@receiver(post_save, sender=Company)
def create_socialnetwork(sender, instance, created, *args, **kwargs):
    if created:
        SocialNetwork.objects.create(company=instance)
