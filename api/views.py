from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


class FirstApiView(APIView):

    def get(self, request, formate=None):
        return Response({"message": "Welcome to Django REST Framework"})
