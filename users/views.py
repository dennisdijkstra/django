from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer
from .models import CustomUser

@api_view(['GET', 'POST'])
def userViews(request):
  if request.method == 'GET':
      return getUsers(request)
  elif request.method == 'POST':
      return createUser(request)

@api_view(['PATCH'])
def updateUser(request):
  return Response('PATCH')

@api_view(['DELETE'])
def deleteUser(request):
  return Response('DELETE')

def getUsers(request):
  users = CustomUser.objects.all()
  serializer = UserSerializer(users, many=True)

  return Response(serializer.data)

def createUser(request):
  serializer = UserSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)