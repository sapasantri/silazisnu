import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from silazisnu.models import SilazisnuModel

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Organization(SilazisnuModel):
    pc      = models.IntegerField(default=0)
    mwc     = models.IntegerField(default=0)
    ranting = models.IntegerField(default=0)
    level   = models.IntegerField(default=0)
    nama    = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name = _('organization')

    def __str__(self):
        return self.nama


class Jabatan(SilazisnuModel):
    nama = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('jabatan')

    def __str__(self):
        return self.nama
