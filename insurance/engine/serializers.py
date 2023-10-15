from rest_framework import serializers
from .helper import calculate_all_insurance
MARITAL_CHOICES = (
    ('single', 'SINGLE'),
    ('married', 'MARRIED'),
)


class UserInsuranceSerializer(serializers.Serializer):
    age = serializers.IntegerField(min_value=0)
    dependents = serializers.IntegerField(min_value=0)
    house = serializers.JSONField(required=False)
    income = serializers.IntegerField(min_value=0)
    marital_status = serializers.ChoiceField(choices=MARITAL_CHOICES)
    risk_questions = serializers.ListField(
        child=serializers.IntegerField(min_value=0, max_value=1)
    )
    vehicle = serializers.JSONField(required=False)

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        return super(UserInsuranceSerializer, self).create(validated_data)

    def save(self, **kwargs):
        # save in db
        # calculate insurance
        return calculate_all_insurance(self.validated_data)
