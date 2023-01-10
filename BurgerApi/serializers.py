from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from datetime import datetime, timedelta


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'password')

        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }}

    def create(self, validated_data):
        hash_password = make_password(validated_data['password'])
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserType
        fields = '__all__'


class AddOnsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddOns
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        add_ons_data = validated_data.pop('add_ons')
        product, created = Product.objects.update_or_create(
            img=validated_data.pop('img'),
            name=validated_data.pop('name'),
            price=validated_data.pop('price'),
            category=category_data,
            add_ons=add_ons_data,
            in_stock=validated_data.pop('in_stock')
        )
        return product


class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = '__all__'

class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        fields = '__all__'

class OrderMasterSerializer(serializers.ModelSerializer):
    customer_detail = CustomerDetailSerializer()
    order_status = OrderStatusSerializer()

    class Meta:
        model = OrderMaster
        fields = '__all__'

    def create(self, validated_data):
        customer_data = validated_data.pop('customer_detail')
        customer_detail = CustomerDetailSerializer.create(CustomerDetailSerializer(), validated_data=customer_data)
        order_status_data = validated_data.pop('order_status')
        order_status = OrderStatusSerializer.create(OrderStatusSerializer(), validated_data=order_status_data)
        order_master, created = OrderMaster.objects.update_or_create(
            user_id=validated_data.pop('user_id'),
            customer_detail=customer_detail,
            order_status=order_status,
            payment_type=validated_data.pop('payment_type'),
            total=validated_data.pop('total'),
            delivery_time=(datetime.now() + timedelta(minutes=30)).strftime('%H:%M:%S')
        )
        return order_master

    def update(self, instance, validated_data):
        nested_customer_detail = self.fields['customer_detail']
        nested_order_status = self.fields['order_status']
        nested_customer_detail_instance = instance.customer_detail
        nested_order_status_instance = instance.order_status
        nested_customer_detail_data = validated_data.pop('customer_detail')
        nested_order_status_data = validated_data.pop('order_status')
        nested_customer_detail.update(nested_customer_detail_instance, nested_customer_detail_data)
        nested_order_status.update(nested_order_status_instance, nested_order_status_data)
        return super(OrderMasterSerializer, self).update(instance, validated_data)


class OrderDetailSerializer(serializers.ModelSerializer):
    order_master_id = OrderMasterSerializer()

    class Meta:
        model = OrderDetail
        fields = '__all__'

    def create(self, validated_data):
        order_master_data = validated_data.pop('order_master_id')
        order_master_id = OrderMasterSerializer.create(OrderMasterSerializer(), validated_data=order_master_data)
        order_detail, created = OrderDetail.objects.update_or_create(
            order_master_id=order_master_id,
            product_id=validated_data.pop('product_id'),
            price=validated_data.pop('price'),
            add_ons=validated_data.pop('add_ons'),
            quantity=validated_data.pop('quantity')
        )
        return order_detail

    def update(self, instance, validated_data):
        nested_serializer = self.fields['order_master_id']
        nested_instance = instance.order_master_id
        nested_data = validated_data.pop('order_master_id')
        nested_serializer.update(nested_instance, nested_data)
        return super(OrderDetailSerializer, self).update(instance, validated_data)
