from datetime import date
from django.test import TestCase, Client
from rest_framework import status
from rest_framework.test import APIClient
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..models import Client, Loan, PaymentSchedule


class PaymentScheduleViewSetTestCase(TestCase):

    def setUp(self):
        self.client = Client.objects.create(name='Test Client')
        self.loan = Loan.objects.create(
            client=self.client,
            amount=1000,
            loan_start_date=date.today(),
            number_of_payments=4,
            periodicity='1m',
            interest_rate=0.1
        )
        self.payment_schedule = PaymentSchedule.objects.create(
            loan=self.loan,
            date=date.today(),
            principal=250,
            interest=10
        )
        self.client = APIClient()

    def test_payment_schedule_list(self):
        response = self.client.get('/api/payment-schedules/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_payment_schedule_detail(self):
        response = self.client.get(f'/api/payment-schedules/{self.payment_schedule.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['principal'], 250)


class ModifyPaymentPrincipalTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.client_obj = Client.objects.create(name='Test Client')
        self.loan = Loan.objects.create(
            client=self.client_obj,
            amount=1000,
            loan_start_date='2024-01-01',
            number_of_payments=4,
            periodicity='1m',
            interest_rate=0.1
        )
        self.payment1 = PaymentSchedule.objects.create(
            loan=self.loan,
            date='2024-01-01',
            principal=250,
            interest=7.5
        )
        self.payment2 = PaymentSchedule.objects.create(
            loan=self.loan,
            date='2024-02-01',
            principal=250,
            interest=6.25
        )

    def test_modify_payment_principal(self):
        url = f'/api/payments/{self.payment2.id}/modify-principal/'
        data = {'new_principal': 200}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        updated_payment2 = PaymentSchedule.objects.get(id=self.payment2.id)
        self.assertEqual(updated_payment2.principal, 200)

        updated_payment2.refresh_from_db()  # Refresh from DB to get updated interest
        self.assertAlmostEqual(updated_payment2.interest, 5.0, delta=0.01)

        updated_payment3 = PaymentSchedule.objects.get(id=self.payment3.id)
        self.assertAlmostEqual(updated_payment3.interest, 2.5, delta=0.01)
