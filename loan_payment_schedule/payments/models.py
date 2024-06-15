from django.db import models


class Loan(models.Model):
    PERIODICITY_CHOICES = [
        ("1d", "1 Day"),
        ("5d", "5 Days"),
        ("2w", "2 Weeks"),
        ("3m", "3 Months"),
    ]
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    loan_start_date = models.DateField()
    number_of_payments = models.IntegerField()
    periodicity = models.CharField(max_length=2, choices=PERIODICITY_CHOICES)
    interest_rate = models.DecimalField(max_digits=4, decimal_places=2)


class PaymentSchedule(models.Model):
    loan = models.ForeignKey(Loan, related_name="schedules", on_delete=models.CASCADE)
    date = models.DateField()
    principal = models.DecimalField(max_digits=10, decimal_places=2)
    interest = models.DecimalField(max_digits=10, decimal_places=2)
