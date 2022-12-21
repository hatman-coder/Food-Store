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


    # def get_queryset(self):
    #     queryset = super(OrderViewSet, self).get_queryset()
    #
    #     user_id = self.request.query_params.get('user_id')
    #     if user_id is not None:
    #         queryset = queryset.filter(user=user_id)
    #     else:
    #         queryset = queryset
    #     return queryset



class CustomerViewSet(viewsets.ModelViewSet):
    queryset = CustomerDetail.objects.all()
    serializer_class = CustomerSerializer


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

