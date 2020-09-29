from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

class SilazisnuUserAdmin(UserAdmin):
    list_display = ('email',)
    list_filter = ('is_superuser', 'is_active')
    search_fields = ('email',)
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('email', 'password1', 'password2'),
    #     }),
    # )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {
            'fields': ()
        }),
        (_('Permissions'), {
            'fields': ('is_active', 'is_superuser'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )
    ordering = ('email',)
    filter_horizontal = ()
