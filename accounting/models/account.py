from django.db import models

from .agreement import Agreement
from .bank import Bank
from .type_account import TypeAccount


class Account(models.Model):
    """Аккаунт"""

    account_type = models.ForeignKey(
        TypeAccount, verbose_name="Тип аккаунта", on_delete=models.CASCADE
    )
    bank = models.ForeignKey(Bank, verbose_name="Банк", on_delete=models.CASCADE)
    agreement = models.ForeignKey(
        Agreement, verbose_name="Договор", on_delete=models.CASCADE
    )
    account = models.CharField(
        verbose_name="Номер инвестиционного счета", max_length=255
    )

    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return self.account
