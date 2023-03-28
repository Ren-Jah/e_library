from django.contrib import admin
from django.shortcuts import redirect

from reader.models import Reader


@admin.action(description='Измененяет статус активности читателя')
def change_active_status(modeladmin, request, queryset):
    queryset.update(is_active=False)


@admin.action(description='Удаляет все книги у пользователя')
def delete_active_books(modeladmin, request, objs):
    for i in objs:
        i.active_books.clear()
    return redirect('.')


class ReaderAdmin(admin.ModelAdmin):
    list_display = ("name", "surname", "display_active_books", "phone_num", "is_active")
    list_filter = ("name", "surname")
    actions = [change_active_status, delete_active_books]

    def display_active_books(self, obj):
        return ', '.join([book.title for book in obj.active_books.all()])

    display_active_books.short_description = 'Взятые книги'


admin.site.register(Reader, ReaderAdmin)
