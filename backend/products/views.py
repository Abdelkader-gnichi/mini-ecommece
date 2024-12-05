from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 

# Create your views here.

class HelloListView(APIView):

    def get(self, request, format=None):
        return Response({"detail":"hello world"}, status.HTTP_200_OK)