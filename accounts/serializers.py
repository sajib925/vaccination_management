from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.login.serializers import LoginSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    USER_TYPE_CHOICES = (
        ('doctor', 'doctor'),
        ('patient', 'patient'),
    )
    role = serializers.ChoiceField(choices=USER_TYPE_CHOICES, required=False, default='patient')
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'first_name', 'last_name', 'role')

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['first_name'] = self.validated_data.get('first_name', '')
        data['last_name'] = self.validated_data.get('last_name', '')
        data['role'] = self.validated_data.get('role', 'patient')
        return data

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.role = self.cleaned_data.get('role', 'patient')
        user.save()
        return user


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'}, required=True, trim_whitespace=False)
    
    class Meta:
        model = User
        fields = ['username', 'password']
