from django.db import models
from author.models import BaseModel, Author


class Book(BaseModel):
    """
    Модель класса  Book
    """
    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    title = models.CharField(verbose_name="Название", max_length=255)
    description = models.TextField(verbose_name="Описание", null=True, blank=True)
    pages_amount = models.PositiveBigIntegerField(verbose_name="Количество страниц")
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.PROTECT)
    quantity_in = models.PositiveIntegerField(verbose_name="Количество книг")

    def __str__(self):
        return f'{self.title}'


