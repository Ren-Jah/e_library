from django.contrib import admin
from django.utils.html import format_html

from book.models import Book
from author.models import Author
from django.urls import reverse

@admin.action(description='Обнуляет количество книг')
def set_quantity_in_zero(modeladmin, request, queryset):
    queryset.update(quantity_in=0)


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "pages_amount", "author", "quantity_in")
    list_filter = ("title", "author")
    list_display_links = ("author", )
    actions = [set_quantity_in_zero]

    # def author_link(self, obj):
    #     cust = obj.author
    #     url = reverse("admin:e_library_book_author") + cust.pk
    #     return format_html(f'<a href="{url}">{cust}</a>')


admin.site.register(Book, BookAdmin)



