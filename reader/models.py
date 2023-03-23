from django.db import models
from book.models import BaseModel, Book


class Reader(BaseModel):
    """
       Модель класса  Reader
       """

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    phone_num = models.CharField(verbose_name="Телефонный номер", max_length=10)
    is_active = models.BooleanField(verbose_name="Статус", default=True)
    active_books = models.ManyToManyField(Book, max_length=3)

    def __str__(self):
        return f'{self.name} {self.surname}'
