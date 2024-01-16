from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CreateUserSerializer

@api_view(['GET'])
def getUser(request):
  return Response('GET')

@api_view(['POST'])
def createUser(request):
  serializer = CreateUserSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
def updateUser(request):
  return Response('PATCH')

@api_view(['DELETE'])
def deleteUser(request):
  return Response('DELETE')