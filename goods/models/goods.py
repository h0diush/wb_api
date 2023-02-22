from django.db import models


class Good(models.Model):
    name = models.CharField(
        "Название товара",
        max_length=255
    )
    price = models.DecimalField(decimal_places=2, max_digits=7,
                                verbose_name="Цена")
    goods_id = models.PositiveSmallIntegerField("ID товара", unique=True,
                                                primary_key=True)
    root_id = models.PositiveSmallIntegerField("ROOT товара")
    user = models.ForeignKey('users.User', models.CASCADE, 'goods',
                             verbose_name='Пользователь')
    date = models.DateTimeField('Дата создания', auto_now_add=True)

    reviews = models.ManyToManyField(
        'goods.Review', related_name='goods_reviews', blank=True,
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
