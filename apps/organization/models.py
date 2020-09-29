import datetime
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.functions import Length

from silazisnu.models import SilazisnuModel

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Organization(SilazisnuModel):
    pc      = models.IntegerField(default=0)
    mwc     = models.IntegerField(default=0)
    ranting = models.IntegerField(default=0)
    jpzis   = models.IntegerField(default=0)
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


class Author(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('authors')

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, related_name="author", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = _('book')

    def __str__(self):
        return '%s - %s' % (self.title, self.author)
