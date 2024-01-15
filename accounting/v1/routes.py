from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    AgreementViewSet,
    TypeAccountViewSet,
    BankViewSet,
    AccountViewSet,
)

app_name = "accounting"
urlpatterns = []
router = DefaultRouter()
router.register(r"agreement", AgreementViewSet, basename="agreement")
router.register(r"type-account", TypeAccountViewSet, basename="type-account")
router.register(r"bank", BankViewSet, basename="bank")
router.register(r"account", AccountViewSet, basename="account")

urlpatterns += router.urls
