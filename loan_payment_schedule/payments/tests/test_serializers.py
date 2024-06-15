from django.test import TestCase
from loan_payment_schedule.payments.models import Client, Loan, PaymentSchedule
from loan_payment_schedule.payments.serializers import ClientSerializer, LoanSerializer, PaymentScheduleSerializer
from datetime import date


class ClientSerializerTestCase(TestCase):

    def test_client_serializer(self):
        client = Client.objects.create(name='Test Client')
        serializer = ClientSerializer(client)
        self.assertEqual(serializer.data['name'], 'Test Client')


class LoanSerializerTestCase(TestCase):

    def test_loan_serializer(self):
        client = Client.objects.create(name='Test Client')
        loan = Loan.objects.create(
            client=client,
            amount=1000,
            loan_start_date=date.today(),
            number_of_payments=4,
            periodicity='1m',
            interest_rate=0.1
        )
        serializer = LoanSerializer(loan)
        self.assertEqual(serializer.data['amount'], 1000)


class PaymentScheduleSerializerTestCase(TestCase):

    def test_payment_schedule_serializer(self):
        client = Client.objects.create(name='Test Client')
        loan = Loan.objects.create(
            client=client,
            amount=1000,
            loan_start_date=date.today(),
            number_of_payments=4,
            periodicity='1m',
            interest_rate=0.1
        )
        payment_schedule = PaymentSchedule.objects.create(
            loan=loan,
            date=date.today(),
            principal=250,
            interest=10
        )
        serializer = PaymentScheduleSerializer(payment_schedule)
        self.assertEqual(serializer.data['principal'], 250)
