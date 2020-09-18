from django.contrib import admin
from .models import (Organization)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pc', 'mwc', 'ranting', 'level', 'nama')
    list_filter = ('pc', 'mwc', 'ranting', 'level', 'nama')
