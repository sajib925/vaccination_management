from rest_framework import serializers
from .models import CommentModel

class CommentModelSerializer(serializers.ModelSerializer):
    patient_username = serializers.ReadOnlyField(source='patient.username')
    campaign_name = serializers.ReadOnlyField(source='campaign.name')

    class Meta:
        model = CommentModel
        fields = ['id', 'patient_username', 'campaign', 'campaign_name', 'comment', 'created_at', 'updated_at']
