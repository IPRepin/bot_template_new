from django.db import models


class TimeBasedModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


"""Создание таблицы акций"""


class Stocks(TimeBasedModel):
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = 'Акции'

    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Название акции")
    description = models.TextField(verbose_name='Описание акции')
    image = models.TextField(verbose_name='ID или ссылка на изображение')

    def __str__(self):
        return f"{self.name}\n" \
               f"{self.description}"


"""Создание таблицы услуг"""


class Services(TimeBasedModel):
    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = 'Услуги'

    id = models.AutoField(primary_key=True)
    name = models.TextField(verbose_name="Название Услуги")
    description = models.TextField(verbose_name='Описание услуги')
    image = models.TextField(verbose_name='ID или ссылка на изображение')

    def __str__(self):
        return f"{self.name}\n" \
               f"{self.description}"