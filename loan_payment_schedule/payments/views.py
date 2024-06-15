from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Loan, PaymentSchedule
from .serializers import LoanSerializer, PaymentScheduleSerializer
from .utils import generate_payment_schedule, recalculate_payments


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        loan = serializer.save()
        generate_payment_schedule(loan)
        return Response(self.get_serializer(loan).data, status=status.HTTP_201_CREATED)


class PaymentScheduleViewSet(viewsets.ModelViewSet):
    queryset = PaymentSchedule.objects.all()
    serializer_class = PaymentScheduleSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_principal = request.data.get('principal', instance.principal)
        instance.principal = new_principal
        instance.save()
        recalculate_payments(instance.loan)
        return Response(self.get_serializer(instance).data)
