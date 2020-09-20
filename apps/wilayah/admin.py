from django.contrib import admin
from .models import (Propinsi)


@admin.register(Propinsi)
class PropinsinAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama')
    list_filter = ('kode', 'nama')
