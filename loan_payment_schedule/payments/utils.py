from .models import PaymentSchedule
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta


def generate_payment_schedule(loan):
    start_date = loan.loan_start_date
    amount = loan.amount
    periodicity = loan.periodicity
    number_of_payments = loan.number_of_payments
    interest_rate = loan.interest_rate
    remaining_balance = amount

    for i in range(1, number_of_payments + 1):
        if periodicity.endswith('d'):
            payment_date = start_date + timedelta(days=int(periodicity[:-1]) * i)
        elif periodicity.endswith('w'):
            payment_date = start_date + timedelta(weeks=int(periodicity[:-1]) * i)
        elif periodicity.endswith('m'):
            payment_date = start_date + relativedelta(months=int(periodicity[:-1]) * i)

        interest = remaining_balance * (interest_rate / number_of_payments)
        principal = (amount / number_of_payments)
        remaining_balance -= principal

        PaymentSchedule.objects.create(
            loan=loan,
            date=payment_date,
            principal=principal,
            interest=interest
        )


def recalculate_payments(loan):
    schedules = PaymentSchedule.objects.filter(loan=loan).order_by('date')
    remaining_balance = loan.amount

    for schedule in schedules:
        interest = remaining_balance * (loan.interest_rate / loan.number_of_payments)
        schedule.interest = interest
        remaining_balance -= schedule.principal
        schedule.save()
