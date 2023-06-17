from django.db import models


class News(models.Model):
    news_title = models.CharField(max_length=64, verbose_name='Заголовок новости')
    news_text1 = models.TextField(max_length=1024, verbose_name='Текст 1')
    news_text2 = models.TextField(max_length=1024, verbose_name='Текст 2', blank=True)
    news_text3 = models.TextField(max_length=1024, verbose_name='Текст 3', blank=True)
    news_text4 = models.TextField(max_length=1024, verbose_name='Текст 4', blank=True)

    def __str__(self):
        return self.news_title
