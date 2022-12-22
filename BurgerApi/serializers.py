from rest_framework import serializers
from .models import *


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
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        exclude = ['id']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ['in_stock']

    def create(self, validated_data):
        category_data = validated_data.pop('category')
        add_ons_data = validated_data.pop('add_ons')
        product, created = Product.objects.update_or_create(category=category_data,
                                                            add_ons=add_ons_data,
                                                            img=validated_data.pop('img'),
                                                            name=validated_data.pop('name'),
                                                            price=validated_data.pop('price'))
        return product


class OrderMasterSerializer(serializers.ModelSerializer):
    customer_detail = CustomerSerializer()

    class Meta:
        model = OrderMaster
        fields = '__all__'

    def create(self, validated_data):
        customer_data = validated_data.pop('customer_detail')
        customer_detail = CustomerSerializer.create(CustomerSerializer(), validated_data=customer_data)
        order_master, created = OrderMaster.objects.update_or_create(
            user_id=validated_data.pop('user_id'),
            customer_detail=customer_detail
        )
        return order_master

    def update(self, instance, validated_data):
        nested_serializer = self.fields['customer_detail']
        nested_instance = instance.customer_detail
        nested_data = validated_data.pop('customer_detail')
        nested_serializer.update(nested_instance, nested_data)
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
