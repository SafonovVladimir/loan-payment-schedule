from rest_framework.routers import DefaultRouter
from .views import LoanViewSet, PaymentScheduleViewSet

router = DefaultRouter()
router.register(r"loans", LoanViewSet)
router.register(r"schedules", PaymentScheduleViewSet)

urlpatterns = router.urls
