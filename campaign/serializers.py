from rest_framework import serializers
from .models import CampaignModel, VaccinesModel, ScheduleModel



class CampaignModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignModel
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class VaccinesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinesModel
        fields = ['id', 'name']

class ScheduleModelSerializer(serializers.ModelSerializer):
    campaign_name = serializers.ReadOnlyField(source='campaign.name')
    vaccine_name = serializers.ReadOnlyField(source='vaccine.name')

    class Meta:
        model = ScheduleModel
        fields = ['id', 'campaign', 'campaign_name', 'vaccine', 'vaccine_name', 'date']

