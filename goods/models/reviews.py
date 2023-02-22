from django.db import models


class Review(models.Model):
    author = models.CharField('Автор отзыва', max_length=75)
    country = models.CharField("Страна автора", max_length=15)
    text = models.CharField('Текст отзыва', max_length=255)
    rating = models.PositiveSmallIntegerField('Оценка')
    good = models.ForeignKey(
        'goods.Good', models.CASCADE, 'reviews_info',
        verbose_name='Товар'
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.author} {self.pk}"
