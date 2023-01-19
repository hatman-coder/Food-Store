from http.client import HTTPResponse
from urllib import request
from rest_framework import viewsets
from .models import *
from .serializers import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from django.db.models import Q

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


class OrderStatusViewset(viewsets.ModelViewSet):
    queryset = OrderStatus.objects.all()
    serializer_class = OrderStatusSerializer

class PaymentTypeViewset(viewsets.ModelViewSet):
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer

class AddOnsViewSet(viewsets.ModelViewSet):
    queryset = AddOns.objects.all()
    serializer_class = AddOnsSerializer

class CategorizedAddOnsViewSet(APIView):
    queryset = AddOns.objects.all()
    serializer_class = AddOnsSerializer

    def get(self, request, format=None):
        query_param= self.request.query_params.get('category')
        addOns = AddOns.objects.filter(category=query_param)
        serializer = AddOnsSerializer(addOns, many=True)
        return Response(serializer.data)

