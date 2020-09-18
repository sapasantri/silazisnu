from django.db import models
from django.utils.translation import gettext_lazy as _

class SilazisnuModel(models.Model):
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Unselect this instead of deleting accounts.'
        ),
    )

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('Silazisnu model')
        abstract = True
