from django.db import models


class Bank(models.Model):
    """Банк"""

    name = models.CharField(verbose_name="Полное наименование банка", max_length=255)
    name_short = models.CharField(
        verbose_name="Краткое наименование банка", max_length=255
    )
    inn = models.CharField(verbose_name="ИНН", max_length=255)
    bik = models.CharField(verbose_name="БИК", max_length=255)
    cor_account = models.CharField(verbose_name="Номер корсчета", max_length=255)
    number_account = models.CharField(
        verbose_name="Номер банковского счета", max_length=255
    )
    city = models.CharField(verbose_name="Краткое наименование банка", max_length=255)

    class Meta:
        verbose_name = "Банк"
        verbose_name_plural = "Банки"

    def __str__(self):
        return self.name
