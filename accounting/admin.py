from django.contrib import admin

from .models import Agreement, Bank, TypeAccount, Account


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Agreement._meta.fields]


@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Bank._meta.fields]


@admin.register(TypeAccount)
class TypeAccountAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in TypeAccount._meta.fields]


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = [field.attname for field in Account._meta.fields]
