from django.contrib import admin
from django.contrib.auth.models import Group

from author.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "surname")
    search_fields = ("name", "surname")


admin.site.register(Author, AuthorAdmin)

admin.site.unregister(Group)
