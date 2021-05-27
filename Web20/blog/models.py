from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Описание', max_length=250)
    full_text=models.TextField('Текст блога')
    date = models.DateTimeField('Время публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'