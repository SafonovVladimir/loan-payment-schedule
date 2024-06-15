from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Loan, PaymentSchedule, Client
from .serializers import LoanSerializer, PaymentScheduleSerializer, ClientSerializer
from .utils import generate_payment_schedule, recalculate_payments


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        loan = serializer.save()
        generate_payment_schedule(loan)
        return Response(self.get_serializer(loan).data, status=status.HTTP_201_CREATED)


class PaymentScheduleViewSet(viewsets.ViewSet):
    queryset = PaymentSchedule.objects.all()
    serializer_class = PaymentScheduleSerializer

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        new_principal = request.data.get("principal", instance.principal)
        instance.principal = new_principal
        instance.save()
        recalculate_payments(instance.loan)
        return Response(self.get_serializer(instance).data)

    def list(self, request):
        payment_schedules = PaymentSchedule.objects.all()
        grouped_by_client = {}

        for schedule in payment_schedules:
            client_id = schedule.loan.client.id
            if client_id not in grouped_by_client:
                grouped_by_client[client_id] = {
                    'client_name': schedule.loan.client.name,
                    'schedules': []
                }
            grouped_by_client[client_id]['schedules'].append(PaymentScheduleSerializer(schedule).data)

        return Response(list(grouped_by_client.values()))


class ScheduleDetailView(APIView):
    def patch(self, request, payment_id):
        try:
            schedule = PaymentSchedule.objects.get(pk=payment_id)
        except PaymentSchedule.DoesNotExist:
            return Response({'error': 'Schedule not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = PaymentScheduleSerializer(schedule, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
