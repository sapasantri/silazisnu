from django.contrib import admin
from .models import (Organization, Jabatan, Author, Book)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('pc', 'mwc', 'ranting', 'jpzis', 'level', 'nama')
    list_filter = ('pc', 'mwc', 'ranting', 'jpzis', 'level', 'nama')


@admin.register(Jabatan)
class JabatanAdmin(admin.ModelAdmin):
    list_display = ('nama',)
    list_filter = ('nama',)


#answer == Book
class BookTabularInline(admin.TabularInline):
    model = Book


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookTabularInline]
    class Meta:
        model = Author


admin.site.register(Author, AuthorAdmin)
admin.site.register(Book)
