from http.client import HTTPResponse
from urllib import request
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerDetail.objects.all()
    serializer_class = CustomerSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
