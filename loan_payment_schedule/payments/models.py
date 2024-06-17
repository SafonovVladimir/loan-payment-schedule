from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Loan(models.Model):
    PERIODICITY_CHOICES = [
        ("1d", "1 Day"),
        ("5d", "5 Days"),
        ("2w", "2 Weeks"),
        ("3m", "3 Months"),
    ]

    client = models.ForeignKey(Client, related_name="loans", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_start_date = models.DateField()
    number_of_payments = models.IntegerField()
    periodicity = models.CharField(max_length=2, choices=PERIODICITY_CHOICES)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"Loan of {self.amount} for {self.client.name}"


class PaymentSchedule(models.Model):
    loan = models.ForeignKey(Loan, related_name="payment_schedules", on_delete=models.CASCADE)
    date = models.DateField()
    principal = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment Schedule for Loan {self.loan_id} on {self.date}"
