import json
from rest_framework import exceptions, generics, response, views, viewsets

from ..models import Agreement, Bank, TypeAccount, Account
from .serializers import (
    AgreementSerializer,
    BankSerializer,
    TypeAccountSerializer,
    AccountSerializer,
)


class AgreementViewSet(viewsets.ModelViewSet):
    queryset = Agreement.objects.all()
    serializer_class = AgreementSerializer


class BankViewSet(viewsets.ModelViewSet):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class TypeAccountViewSet(viewsets.ModelViewSet):
    queryset = TypeAccount.objects.all()
    serializer_class = TypeAccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
