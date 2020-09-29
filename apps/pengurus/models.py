from django.db import models
from django.utils.translation import gettext_lazy as _
from silazisnu.models import SilazisnuAbstractUser
from apps.organization.models import (Jabatan, Organization )


class User(SilazisnuAbstractUser):
    full_name = models.CharField(_("Nama Lengkap"), max_length=50)
    phone = models.CharField(max_length=20, blank=True, null=True)
    jabatan = models.ForeignKey(Jabatan, verbose_name=_("jabatan"),
                                on_delete=models.CASCADE, blank=True, null=True)
    menjabat = models.ForeignKey(Organization, verbose_name=_("menjabat"),
                                on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = _('user')

    def __str__(self):
        return '%s' % (self.full_name)
