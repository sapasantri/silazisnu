from django.contrib import admin
from .models import (Organization, Jabatan)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pc', 'mwc', 'ranting', 'level', 'nama')
    list_filter = ('pc', 'mwc', 'ranting', 'level', 'nama')

@admin.register(Jabatan)
class JabatanAdmin(admin.ModelAdmin):
    list_display = ('nama',)
    list_filter = ('nama',)
