from rest_framework import serializers

from ..models import Agreement, Bank, TypeAccount, Account


class AgreementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agreement
        fields = "__all__"


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = "__all__"


class TypeAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAccount
        fields = "__all__"


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"
        depth = 3
