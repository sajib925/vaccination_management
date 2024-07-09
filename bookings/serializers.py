from rest_framework import serializers
from datetime import timedelta
from .models import BookingModel
from campaign.models import CampaignModel, VaccinesModel

class BookingModelSerializer(serializers.ModelSerializer):
    patient_username = serializers.ReadOnlyField(source='patient.username')
    campaign_name = serializers.ReadOnlyField(source='campaign.name')
    vaccine_name = serializers.ReadOnlyField(source='vaccine.name')

    class Meta:
        model = BookingModel
        fields = ['id', 'patient', 'patient_username', 'campaign', 'campaign_name', 'vaccine', 'vaccine_name', 'nid', 'age', 'first_dose_date', 'second_dose_date', 'medical_info', 'created_at', 'updated_at']
        read_only_fields = ['second_dose_date']

    def create(self, validated_data):
        booking = BookingModel.objects.create(**validated_data)
        booking.second_dose_date = booking.first_dose_date + timedelta(days=28)
        booking.save()
        return booking
