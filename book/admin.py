from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

import author
from book.models import Book
from author.models import Author


@admin.action(description='Обнуляет количество книг')
def set_quantity_in_zero(modeladmin, request, queryset):
    queryset.update(quantity_in=0)


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "pages_amount", "author_link", "quantity_in")
    list_filter = ("title", "author")
    actions = [set_quantity_in_zero]

    def author_link(self, obj):
        author_id = obj.author.id
        url = reverse("admin:author_author_change", args=[author_id])
        return format_html(f'<a href="{url}">{author_id}</a>')






admin.site.register(Book, BookAdmin)



