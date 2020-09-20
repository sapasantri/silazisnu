from django.db import models
from django.utils.translation import gettext_lazy as _
from silazisnu.models import SilazisnuModel

class Propinsi(SilazisnuModel):
    nama    = models.models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = _('propinsi')

    def __str__(self):
        return self.nama
