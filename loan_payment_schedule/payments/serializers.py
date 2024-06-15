from rest_framework import serializers
from .models import Loan, PaymentSchedule


class PaymentScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentSchedule
        fields = ["id", "date", "principal", "interest"]


class LoanSerializer(serializers.ModelSerializer):
    schedules = PaymentScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Loan
        fields = ["id", "amount", "loan_start_date", "number_of_payments", "periodicity", "interest_rate", "schedules"]

    def validate_periodicity(self, value):
        if value not in dict(Loan.PERIODICITY_CHOICES).keys():
            raise serializers.ValidationError("Invalid periodicity value.")
        return value
