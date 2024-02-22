"""
Модели для приложения "Jobs" (выполненные работы).
"""

from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

from base.models import TimeStampMixin


class Job(TimeStampMixin):
    """
    Модель для хранения данных о работах.
    """

    image = models.ImageField(
        upload_to="images/",
        verbose_name="Изображение",
        help_text="Изображение для демонстрации работы",
    )
    description = models.CharField(
        max_length=255,
        verbose_name="Описание",
        help_text="Краткое описание выполненной работы",
    )
    indepth_description = RichTextUploadingField(
        verbose_name="Подробное описание",
        help_text="Подробное описание выполненной работы",
    )

    def summary(self) -> str:
        """
        Краткое содержание сообщения.

        :return:
        """

        return self.indepth_description[:100] + "..."

    class Meta:
        verbose_name = "Выполненная работа"
        verbose_name_plural = "Выполненные работы"

    def __str__(self) -> str:
        return f'Объект "Выполненная работа" (id={self.pk})'
