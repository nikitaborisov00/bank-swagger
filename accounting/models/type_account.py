from django.db import models


class TypeAccount(models.Model):
    """Тип аккаунта"""

    class TypesOfAccount(models.TextChoices):
        BROKERAGE = "BROKERAGE", "Брокерский"
        DEALER = "DEALER", "Дилерский"
        MANAGEMENT = "MANAGEMENT", "Управления"

    acc_type = models.CharField(
        verbose_name="Тип аккаунта", choices=TypesOfAccount.choices, max_length=255
    )

    class Meta:
        verbose_name = "Тип аккаунта"
        verbose_name_plural = "Типы аккаунтов"

    def __str__(self):
        return self.acc_type
