from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models
from book.models import BaseModel, Book
from reader.validators import validate_phone_num


class UserRoles(models.TextChoices):
    OWNER = 'owner'
    ADMIN = 'admin'


class Reader(AbstractUser):
    """ Модель класса  Reader  """

    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    phone_num = models.CharField(unique=True, verbose_name="Телефонный номер", max_length=30, validators=[validate_phone_num])
    is_active = models.BooleanField(verbose_name="Статус", default=True)
    active_books = models.ManyToManyField(Book, max_length=3, blank=True)
    role = models.CharField(choices=UserRoles.choices, default=UserRoles.OWNER, max_length=20)

    class Meta:
        verbose_name = "Читатель"
        verbose_name_plural = "Читатели"

    def __str__(self):
        return f'{self.name} {self.surname}'
