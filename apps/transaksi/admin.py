from django.contrib import admin
from .models import (Penerimaan)


@admin.register(Penerimaan)
class PenerimaanAdmin(admin.ModelAdmin):
    #all Field
    list_display = [field.name for field in Penerimaan._meta.get_fields()]
