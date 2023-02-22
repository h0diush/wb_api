from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        "users.User", models.CASCADE, verbose_name="Пользователь"
    )
    telegram_id = models.CharField("Телеграм ID", max_length=25, null=True,
                                   blank=True)

    class Meta:
        verbose_name = "Профиль пользователя"
        verbose_name_plural = "Профили пользователей"

    def __str__(self):
        return f"{self.user} profile ({self.telegram_id})"
