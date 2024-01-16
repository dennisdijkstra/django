from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .models import CustomUser

class CreateUserSerializer(serializers.ModelSerializer):
  password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

  class Meta:
    model = CustomUser
    fields = ['email', 'password', 'password2']
    extra_kwargs = {
        'password': {'write_only': True}
    }

  def save(self):
    user = CustomUser(email=self.validated_data['email'])
    password = self.validated_data['password']
    password2 = self.validated_data['password2']
    
    if password != password2:
        raise serializers.ValidationError({'password': 'Passwords must match.'})
      
    try:
      validate_password(password)
    except ValidationError as err:
      raise serializers.ValidationError({'password': err.messages })

    user.set_password(password)
    user.save()

    return user