from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from loan_payment_schedule.payments.models import Loan, PaymentSchedule
from loan_payment_schedule.payments.utils import generate_payment_schedule


class LoanAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_loan(self):
        response = self.client.post("/api/loans/", {
            "amount": 1000,
            "loan_start_date": "2024-10-01",
            "number_of_payments": 4,
            "periodicity": "1m",
            "interest_rate": 0.1
        }, format="json")
        # This should fail because "1m" is not a valid choice.
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response = self.client.post("/api/loans/", {
            "amount": 1000,
            "loan_start_date": "2024-10-01",
            "number_of_payments": 4,
            "periodicity": "1d",
            "interest_rate": 0.1
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Loan.objects.count(), 1)
        self.assertEqual(PaymentSchedule.objects.count(), 4)

    def test_update_payment(self):
        loan = Loan.objects.create(
            amount=1000,
            loan_start_date="2024-10-01",
            number_of_payments=4,
            periodicity="1d",
            interest_rate=0.1
        )
        generate_payment_schedule(loan)
        schedule = PaymentSchedule.objects.first()
        response = self.client.patch(f"/api/schedules/{schedule.id}/", {
            "principal": 50
        }, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        schedule.refresh_from_db()
        self.assertEqual(schedule.principal, 50)
