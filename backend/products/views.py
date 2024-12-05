from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class ProductListView(APIView):


    def get(self, request, format=None):
        products = Product.objects.all()
        in_stock = self.request.query_params.get('in_stock', None)
        
        if in_stock is not None:
            in_stock = in_stock.lower() == 'true'
            products = products.filter(stock__gt=0) if in_stock else products.filter(stock=0)
        
        serializer = ProductSerializer(products, many=True)
        

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        data = request.data
        serializer = ProductSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            product_instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProductDetailView(APIView):

    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, many=False)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk, format=None):
        data = request.data
        product = self.get_object(pk)

        serializer = ProductSerializer(product, data=data)

        if serializer.is_valid(raise_exception=True):
            product_instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.delete()
        return Response({"detail":"product was deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        