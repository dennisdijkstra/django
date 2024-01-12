from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getUsers(request):
  person = {
    'name': 'Dennis',
    'age': 28
  }

  return Response(person)
