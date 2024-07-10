from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    USER_TYPE_CHOICES = (
        ('patient', 'patient'),
        ('doctor', 'doctor'),
        
    )
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES, default='patient')

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['user_type'] = self.validated_data.get('user_type', 'patient')
        print('welcome ', data['user_type'])
        return data

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data.get('user_type')
        user.save()
        return user
