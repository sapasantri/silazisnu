from django.contrib import admin

from silazisnu.admin import SilazisnuUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User

@admin.register(User)
class UserAdmin(SilazisnuUserAdmin):
    list_display = ('email', 'full_name')
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('full_name', 'email')
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('username', 'email', 'full_name', 'password1', 'password2'),
    #     }),
    # )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        (_('Personal info'), {
            'fields': ('full_name', 'phone')
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_superuser'),
        }),
        (_('Jabatan'), {
            'fields': ('jabatan', 'menjabat')
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )
    # inlines = (EmployeeInline,)
    ordering = ('email',)
    filter_horizontal = ()
