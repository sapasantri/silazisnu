from django.db import models
from django.utils.translation import gettext_lazy as _
from silazisnu.models import SilazisnuModel
from apps.pengurus.models import User
from apps.organization.models import Organization



class Penerimaan(SilazisnuModel):
    date_transaction = models.DateField()
    organisasi = models.ForeignKey(
        Organization, blank=True, null=True, related_name="organisasi", on_delete=models.CASCADE)
    entryer = models.ForeignKey(User, related_name="entryer", on_delete=models.CASCADE)
    nominal = models.IntegerField(default=0)
    note = models.TextField()

    class Meta:
        verbose_name = _('penerimaan')

    def __str__(self):
        return "%s - %s" % (self.entryer, self.nominal)
