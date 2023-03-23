from django.db import models


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")

    class Meta:
        abstract = True


class Author(BaseModel):
    """
    Модель класса  Author
    """
    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"

    name = models.CharField(verbose_name="Имя", max_length=255)
    surname = models.CharField(verbose_name="Фамилия", max_length=255)
    photo = models.ImageField(upload_to='author_images', null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


