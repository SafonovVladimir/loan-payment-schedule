from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import LoanViewSet, PaymentScheduleViewSet, ClientViewSet, modify_payment_principal

router = DefaultRouter()
router.register(r"clients", ClientViewSet)
router.register(r"loans", LoanViewSet)
router.register(r"schedules", PaymentScheduleViewSet)

custom_urlpatterns = [
    path('payments/<int:payment_id>/modify-principal/', modify_payment_principal, name='modify_payment_principal'),
]

urlpatterns = [
    path("", include(router.urls)),
    path("", include(custom_urlpatterns)),
]
