from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

  class Meta:
    model = CustomUser
    fields = '__all__'
    extra_kwargs = {
        'password': {'write_only': True}
    }