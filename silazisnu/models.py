from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import NucareUserManager


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


class SilazisnuAbstractUser(SilazisnuModel, AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_("username"), max_length=255, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = NucareUserManager()

    class Meta:
        verbose_name = _('account')
        verbose_name_plural = _('accounts')
        abstract = True
