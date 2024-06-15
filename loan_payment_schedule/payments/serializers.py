from rest_framework import serializers

from .models import Loan, PaymentSchedule, Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name"]


class PaymentScheduleSerializer(serializers.ModelSerializer):
    loan_id = serializers.PrimaryKeyRelatedField(source="loan.id", read_only=True)
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = PaymentSchedule
        fields = ["id", "date", "principal", "interest", "loan_id", "client_name"]

    def get_client_name(self, obj):
        return obj.loan.client.name if obj.loan.client else None


class LoanSerializer(serializers.ModelSerializer):
    schedules = PaymentScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = Loan
        fields = [
            "id",
            "client",
            "amount",
            "loan_start_date",
            "number_of_payments",
            "periodicity",
            "interest_rate",
            "schedules"
        ]

    def get_client_name(self, obj):
        return obj.client.name

    def validate_periodicity(self, value):
        if value not in dict(Loan.PERIODICITY_CHOICES).keys():
            raise serializers.ValidationError("Invalid periodicity value.")
        return value
