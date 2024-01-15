from django.db import models
from django.utils import timezone
from datetime import datetime


class Agreement(models.Model):
    """Договор"""

    agreement_number = models.CharField(
        verbose_name="Номер заключения договора", max_length=255
    )
    date_open = models.DateField(
        verbose_name="Дата заключения договора", default=timezone.now()
    )
    date_close = models.DateField(
        verbose_name="Дата закрытия договора", default=timezone.now()
    )
    note = models.CharField(verbose_name="Пояснения", max_length=255)

    class Meta:
        verbose_name = "Договор"
        verbose_name_plural = "Договора"

    def __str__(self):
        return self.agreement_number
