from django.contrib import admin
from django.contrib.auth.models import Group

from author.models import Author


admin.site.register(Author)

admin.site.unregister(Group)
