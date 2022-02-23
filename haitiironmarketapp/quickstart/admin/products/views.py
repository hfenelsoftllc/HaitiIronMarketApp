#from django.shortcuts import render
from itertools import product
from lzma import FORMAT_ALONE
from random import random
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
#from rest_framework.status import HTTP_200_OK
from .serializers import ProductSerializer
from .models import Product
from .models import User

# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list (self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        product = Product.objects.get(id=pk)        
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.object.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })