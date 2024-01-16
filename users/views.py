import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getUsers(request):
  print(request, id)

  person = {
    'name': 'Dennis',
    'age': 28
  }
  return Response(person)

@api_view(['PATCH'])
def updateUser(request, id):
  print(request, id)
  return Response(id)

@api_view(['DELETE'])
def deleteUser(request, id):
  print(request, id)
  return Response(id)