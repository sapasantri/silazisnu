from django.db import models
from django.utils.translation import gettext_lazy as _
from silazisnu.models import SilazisnuModel

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
