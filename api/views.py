import rest_framework
from products.models import Product
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from api.serializers import FirstSerializer, ProductSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication


@api_view
def testView(request):
    return Response({"message": "Test completed."})


class FirstApiView(APIView):

    serializer_class = FirstSerializer

    def get(self, request, formate=None):
        return Response({"message": "Welcome to Django REST Framework"})

    def post(self, request, formate=None):
        print(type(request.data))
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            return Response({"message": f"Welcome {serializer.validated_data.get('name')}"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, formate=None):
        return Response({"message": "PUT request received."})

    def patch(self, request, formate=None):
        return Response({"message": "PATCH request received."})

    def delete(self, request, formate=None):
        return Response({"message": "DELETE request received."})


class ProductViewSets(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticated]
    # authentication_classes = [TokenAuthentication]
