from django.http import Http404
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser

class UserList(APIView):
  def get(self, request):
    users = CustomUser.objects.all()
    serializer = UserSerializer(users, many=True)

    return Response(serializer.data)
  
  def post(self, request):
    user = CustomUser(email=request.data['email'])
    password = request.data['password']
    password2 = request.data['password2']
    serializer = UserSerializer(data=request.data)  
  
    if password != password2:
      raise serializers.ValidationError({'password': 'Passwords must match.'})

    try:
      validate_password(password)
    except ValidationError as err:
      raise serializers.ValidationError({'password': err.messages })

    if serializer.is_valid():
      user.set_password(password)
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
  def get_user(self, id):
    try:
      return CustomUser.objects.get(id=id)
    except CustomUser.DoesNotExist:
      raise Http404

  def get(self, request, id):
    user = self.get_user(id)
    serializer = UserSerializer(user, many=False)

    return Response(serializer.data)

  def put(self, request, id):
    user = self.get_user(id)
    serializer = UserSerializer(instance=user, data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, id):
    user = self.get_user(id)

    if user:
      user.delete()
  
    return Response(status=status.HTTP_204_NO_CONTENT)