from django.db import models

from users.utilits import generate_code


class CodeForTelegram(models.Model):
    hash_code = models.CharField(max_length=155, verbose_name='Код')
    user = models.OneToOneField('users.User', verbose_name='Пользователь',
                                on_delete=models.CASCADE)

    def __str__(self):
        return f'Код № {self.pk}'

    class Meta:
        verbose_name = 'Код ТГ'
        verbose_name_plural = 'Коды ТГ'

    def save(self, *args, **kwargs):
        self.hash_code = generate_code()
        return super().save(*args, **kwargs)
