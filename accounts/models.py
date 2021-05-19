from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import reverse
from datetime import date


def upload_path(instance, filename):
    return f"{instance.realtor.pk}/avatar/{filename}"


class Profile(models.Model):
    GENDER = [
        (1, "Male"),
        (2, "Famale"),
    ]
    realtor = models.OneToOneField(
        User,
        verbose_name=_("Realtor"),
        on_delete=models.CASCADE,
        db_column="RLTR",
        related_name="profile",
    )
    avatar = models.ImageField(
        _("Profile Picture"),
        upload_to=upload_path,
        blank=True,
        null=True,
        db_column="AVATAR",
    )
    bio = models.TextField(_("Bio"), blank=True, null=True, db_column="BIO")
    phone = models.CharField(
        _("Phone Number"), max_length=20, blank=True, null=True, db_column=""
    )
    is_mvp = models.BooleanField(_("Saler of the Month"), default=False)
    registered = models.DateTimeField(
        _("Registered"), auto_now=False, auto_now_add=True, db_column="RGSTD"
    )
    status = models.BooleanField(_("Account Status"), default=True, db_column="STATUS")
    deactivated_date = models.DateTimeField(
        _("Deactivaed"), blank=True, null=True, db_column="DDATE", editable=False
    )
    gender = models.PositiveIntegerField(
        _("Gender"), choices=GENDER, blank=True, null=True, db_column="GENDER"
    )
    whatsapp = models.CharField(
        _("Whatsapp Number"), max_length=50, blank=True, null=True, db_column="WHTSP"
    )
    telgram = models.CharField(
        _("Telegram Number"), max_length=50, blank=True, null=True, db_column="TLGRM"
    )
    insta = models.CharField(
        _("Instagram Username"), max_length=30, blank=True, null=True, db_column="INSTA"
    )
    twitter = models.CharField(
        _("Twitter Username"), max_length=30, blank=True, null=True, db_column="TWTTR"
    )
    facebook = models.CharField(
        _("Facebook Username"), max_length=30, blank=True, null=True, db_column="FBOOK"
    )

    def __str__(self):
        return str(self.realtor)

    @property
    def email(self):
        email = self.realtor.email
        return email

    @property
    def first_name(self):
        first_name = self.realtor.first_name
        return first_name

    @property
    def last_name(self):
        last_name = self.realtor.last_name
        return last_name

    class Meta:
        db_table = "PROFILE"
        managed = True
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
