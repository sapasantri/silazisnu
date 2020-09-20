from django.db import models
from django.utils.translation import gettext_lazy as _
from silazisnu.models import SilazisnuModel

class Propinsi(SilazisnuModel):
    kode = models.IntegerField(blank=False, null=False)
    nama = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = _('propinsi')

    def __str__(self):
        return '%s - %s' % (self.kode, self.nama)

class Kota(SilazisnuModel):
    propinsi = models.ForeignKey(Propinsi, on_delete=models.CASCADE)
    kode = models.CharField(max_length=50, blank=False, null=False)
    nama = models.CharField(max_length=250, blank=False, null=False)

    class Meta:
        verbose_name = _('Kota')

    def __str__(self):
        return '%s - %s' % (self.kode, self.nama)
