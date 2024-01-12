from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getUsers():
  person = {
    'name': 'Dennis',
    'age': 28
  }

  return Response(person)

@api_view(['PATCH'])
def updateUser():
  return Response('Patch user')

@api_view(['DELETE'])
def deleteUser():
  return Response('Delete user')