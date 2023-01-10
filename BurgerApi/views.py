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


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerDetail.objects.all()
    serializer_class = CustomerDetailSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class OrderMasterViewset(viewsets.ModelViewSet):
    queryset = OrderMaster.objects.all()
    serializer_class = OrderMasterSerializer


class OrderDetailViewset(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    # permission_classes = [IsAuthenticated]
